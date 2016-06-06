Installing Ambari Agents Manually
=================================

In cases where you do not have SSH for Ambari to automatically install the Agents or you want to pre-install the Agents, you can perform a manual agent setup. This involves two steps:

#. Configuring the Ambari Repo
#. Install Ambari Agents

Configuring Ambari Repo
_______________________

Follow the instructions in the section for the operating system that runs your installation host.

RHEL/CentOS
_____________

On a server host that has Internet access, use a command line editor to perform the following steps:

1. Log in too your host as ``root``

2. Add the |fdd| Yum repository to a file called ``/etc/yum.repos.d/ambari.repo``

  **RHEL/CentOS 6.x**

  ::

    [Updates-ambari-2.2.0.0]
    name=ambari-2.2.0.0 - Updates
    baseurl=https://rbp_email_address:password@public-repo.radicalbit.io/ambari/centos6/2.2.0.0
    gpgcheck=1
    gpgkey=https://public-repo.radicalbit.io/repo/RPM-GPG-KEY/RPM-GPG-KEY-Radicalbit.key
    enabled=1
    priority=1

  **RHEL/CentOS 7.x**

  ::

    [Updates-ambari-2.2.0.0]
    name=ambari-2.2.0.0 - Updates
    baseurl=https://rbp_email_address:password@public-repo.radicalbit.io/ambari/centos7/2.2.0.0
    gpgcheck=1
    gpgkey=https://public-repo.radicalbit.io/repo/RPM-GPG-KEY/RPM-GPG-KEY-Radicalbit.key
    enabled=1
    priority=1

  where *rbp_email_address* and *password* are the account credentials you created on the registration page [TODO -> ADD LINK].

  .. Attention::
    Depending on your environment, you might need to replace @ in your email address with %40 and escape any character in your password that is used in your operating system's command line. Examples: \! and \|.

  .. Important::
    Do not modify the ``ambari.repo`` file name. This file is expected to be available on the Ambari Server host during Agent registration.

3. Confirm that the repository is configured by checking the repo list.

  ::

    yum repolist

Install Ambari Agents
_____________________

1. Install the Ambari Agent on every host in your cluster.

  ::

    yum install ambari-agent

2. Using a text editor, configure the Ambari Agent by editing the ``ambari-agent.ini`` file as shown in the following example:

  ::

    vi /etc/ambari-agent/conf/ambari-agent.ini

  ::

    [server]
    hostname=<your.ambari.server.hostname>
    url_port=8440
    secured_url_port=8441

3. Start the agent on every host in your cluster.

  ::

    ambari-agent start

  The agent registers with the Server on start.