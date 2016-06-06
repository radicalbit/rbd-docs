Using Custom Host Names
=======================

You can customize the agent registration host name and the public host name used for each host in Ambari. Use this capability when "hostname" does not return the public network host name for your machines.

How to Customize the name of a host
___________________________________

1. At the ``Install Options`` step in the Cluster Installer wizard, select ``Perform Manual Registration for Ambari Agents``.

2. Install the Ambari Agents manually on each host, as described in Install the :doc:`Ambari Agents Manually<install-agent>`.

3. To know the customized name of the host to which the Ambari agent registers, for every host, create a script like the following example, named ``var/lib/ambari-agent/hostname.sh`` . Be sure to chmod the script so it is executable by the Agent.

  ::

    #!/bin/sh 
    echo <ambari_hostname>

  where ``<ambari_hostname>`` is the host name to use for Agent registration.

4. Open ``/etc/ambari-agent/conf/ambari-agent.ini`` on every host, using a text editor.

5. Add to the ``[agent]`` section the following line:

  ::

    hostname_script=/var/lib/ambari-agent/hostname.sh

  where ``/var/lib/ambari-agent/hostname.sh`` is the name of your custom echo script.

6. To generate a public host name for every host, create a script like the following example, named ``var/lib/ambari-agent/public_hostname.sh`` to show the name for that host in the UI. Be sure to chmod the script so it is executable by the Agent.

  ::

    #!/bin/sh
    <hostname> -f

  where ``<hostname>`` is the host name to use for Agent registration.

7. Open ``/etc/ambari-agent/conf/ambari-agent.ini`` on every host, using a text editor.

8. Add to the ``[agent]`` section the following line:

  ::

    public_hostname_script=/var/lib/ambari-agent/public_hostname.sh

9. If applicable, add the host names to ``/etc/hosts`` on every host.

10. Restart the Agent on every host for these changes to take effect.

  ::

    ambari-agent restart
