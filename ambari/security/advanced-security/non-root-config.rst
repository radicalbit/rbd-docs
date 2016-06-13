Configuring Ambari for Non-Root
===============================

In most secure environments, restricting access to and limiting services that run as root is a hard requirement.
For these environments, Ambari can be configured to operate without direct root access.
Both Ambari Server and Ambari Agent components allow for non-root operation, and the following sections will walk you through the process.

How to Configure Ambari Server for Non-Root
___________________________________________

You can configure the Ambari Server to run as a non-root user.

During the ambari-server setup process, when prompted to ``Customize user account for ambari-server daemon?``, choose ``y``.

The setup process prompts you for the appropriate, non-root user to run the Ambari Server as; for example: ``ambari``.

.. Note::
  The non-root user you choose to run the Ambari Server should be part of the |rbd-stack| group.
  This group must match the service |rbd-stack| group accounts referenced in the ``Customize Services > Misc`` tab during the Install Wizard configuration step.
  The default group name is ``rbp-services`` but if you customized this value during cluster install, be sure to make the non-root user a part of that group.
  See :doc:`Customizing RBD Services</ambari/reference/customize-services>` for more information on service account users and groups.

.. Note::
  If Ambari Server is running as a non-root user, such as 'ambari', and you are planning on using Ambari Views, the following properties in ``Services > HDFS > Configs > Advanced core-site`` must be added:

  ::

    hadoop.proxyuser.ambari.groups=*
    hadoop.proxyuser.ambari.hosts=*

How to Configure an Ambari Agent for Non-Root
_____________________________________________

You can configure the Ambari Agent to run as a non-privileged user as well.
That user requires specific sudo access in order to su to |rbd-stack| service accounts and perform specific privileged commands.
Configuring Ambari Agents to run as non-root requires that you manually install agents on all nodes in the cluster.
For these details, see :doc:`Installing Ambari Agents Manually</ambari/reference/install-agent>`.
After installing each agent, you must configure the agent to run as the desired, non-root user.
In this example we will use the ``ambari`` user.

Change the ``run_as_user property`` in the ``/etc/ambari-agent/conf/ambari-agent.ini`` file, as illustrated below:

::

  run_as_user=ambari

Once this change has been made, the ambari-agent must be restarted to begin running as the non-root user.

The non-root functionality relies on sudo to run specific commands that require elevated privileges as defined in the :ref:`Sudoer Configuration<ambari-sudoer-configuration>`.
The sudo configuration is split into three sections: :ref:`Customizable Users<ambari-customizable-users>`, :ref:`Commands<ambari-commands>`, and :ref:`Sudo Defaults<ambari-sudo-defaults>`.

.. _ambari-sudoer-configuration:

**Sudoer Configuration**

The Customizable Users, Commands, and Sudo Defaults sections will cover how sudo should be configured to enable Ambari to run as a non-root user.
Each of the sections includes the specific sudo entries that should be placed in ``/etc/sudoers`` by running the ``visudo`` command.

.. _ambari-customizable-users:

**Customizable Users**

This section contains the ``su`` commands and corresponding |rbd-stack| service accounts that are configurable on install:

::

  # Ambari Customizable Users
  ambari ALL=(ALL) NOPASSWD:SETENV: /bin/su hdfs *, /bin/su ambari-qa *, /bin/su zookeeper *, /bin/su ams *, /bin/su kafka *, /bin/su cassandra *, /bin/su alluxio *,/bin/su flink *, /bin/su/zeppelin *

.. Note::
  These user accounts must match the service user accounts referenced in the ``Customize Services > Misc`` tab during the Install Wizard configuration step.
  For example, if you customize HDFS to run as ``xyz_hdfs``, modify the su command above to be ``/bin/su xyz_hdfs``.

.. _ambari-commands:

**Commands**

This section contains the specific commands that must be issued for standard agent operations:

::

  # Ambari Commands
  ambari ALL=(ALL) NOPASSWD:SETENV: /usr/bin/yum,/usr/bin/zypper,/usr/bin/apt-get, /bin/mkdir, /usr/bin/test, /bin/ln, /bin/chown, /bin/chmod, /bin/chgrp, /usr/sbin/groupadd, /usr/sbin/groupmod, /usr/sbin/useradd, /usr/sbin/usermod, /bin/cp, /usr/sbin/setenforce, /usr/bin/test, /usr/bin/stat, /bin/mv, /bin/sed, /bin/rm, /bin/kill, /bin/readlink, /usr/bin/pgrep, /bin/cat, /usr/bin/unzip, /bin/tar, /usr/bin/tee, /bin/touch, /usr/bin/hdp-select, /usr/bin/conf-select, /usr/lib/hadoop/sbin/hadoop-daemon.sh, /usr/lib/hadoop/bin/hadoop-daemon.sh, /sbin/chkconfig gmond off, /sbin/chkconfig gmetad off, /etc/init.d/httpd *, /sbin/service hdp-gmetad start, /sbin/service hdp-gmond start, /usr/sbin/gmond, /usr/sbin/update-rc.d ganglia-monitor *, /usr/sbin/update-rc.d gmetad *, /etc/init.d/apache2 *, /usr/sbin/service hdp-gmond *, /usr/sbin/service hdp-gmetad *, /sbin/service mysqld *, /usr/bin/dpkg *, /bin/rpm *, /usr/sbin/hst *

To re-iterate, you must do this sudo configuration on every node in the cluster.
To ensure that the configuration has been done properly, you can ``su`` to the ``ambari`` user and run ``sudo -l``.
There, you can double check that there are no warnings, and that the configuration output matches what was just applied.

.. _ambari-sudo-defaults:

**Sudo Defaults**

Some versions of sudo have a default configuration that prevents sudo from being invoked from a non-interactive shell.
In order for the agent to run it's commands non-interactively, some defaults need to be overridden.

::

  Defaults exempt_group = ambari
  Defaults !env_reset,env_delete-=PATH
  Defaults: ambari !requiretty

To re-iterate, this sudo configuration must be done on every node in the cluster.
To ensure that the configuration has been done properly, you can ``su`` to the ``ambari`` user and run ``sudo -l``.
There, you can double-check that there are no warnings, and that the configuration output matches what was just applied.