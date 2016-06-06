Configure the Ambari Repository
===============================

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

4. Install the Ambari bits. This also installs the default PostgreSQL Ambari database.

  ::

    yum install ambari-server

5. Enter ``y`` when prompted to to confirm transaction and dependency checks.

Complete!

.. Note::
  Ambari Server by default uses an embedded PostgreSQL database. When you install the Ambari Server, the PostgreSQL packages and dependencies must be available for install. These packages are typically available as part of your Operating System repositories. Please confirm you have the appropriate repositories available for the postgresql-server packages.
