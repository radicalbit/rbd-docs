Check DNS and NSCD
==================

All hosts in your system must be configured for both forward and and reverse DNS.

If you are unable to configure DNS in this way, you should edit the ``/etc/hosts`` file on every host in your cluster to contain the IP address and Fully Qualified Domain Name of each of your hosts.
The following instructions are provided as an overview and cover a basic network setup for generic Linux hosts.
Different versions and flavors of Linux might require slightly different commands and procedures.
Please refer to the documentation for the operating system(s) deployed in your environment.

Hadoop relies heavily on DNS, and as such performs many DNS lookups during normal operation.
To reduce the load on your DNS infrastructure, it's highly recommended to use the Name Service Caching Daemon (NSCD) on cluster nodes running Linux.
This daemon will cache host, user, and group lookups and provide better resolution performance, and reduced load on DNS infrastructure.


Edit the Host File
__________________

1. Using a text editor, open the hosts file on every host in your cluster. For example:

  ::

    sudo vi /etc/hosts

2. Add a line for each host in your cluster. The line should consist of the IP address and the FQDN. For example:

  ::

    1.2.3.4 <fully.qualified.domain.name>

  .. Important::
    Do not remove the following two lines from your hosts file. Removing or editing the following lines may cause various programs that require network functionality to fail.
    ::

      127.0.0.1 localhost.localdomain localhost
      ::1 localhost6.localdomain6 localhost6

Set the Hostname
________________

1. Confirm that the hostname is set by running the following command:

  ::

    hostname -f

  This should return the ``<fully.qualified.domain.name>`` you just set.

2. Use the "hostname" command to set the hostname on each host in your cluster. For example:

  ::

    hostname <fully.qualified.domain.name>

Edit the Network Configuration File
___________________________________

1. Using a text editor, open the network configuration file on every host and set the desired network configuration for each host. For example:

  ::

    sudo vi /etc/sysconfig/network

2. Modify the HOSTNAME property to set the fully qualified domain name.

  ::

    NETWORKING=yes
    HOSTNAME=<fully.qualified.domain.name>