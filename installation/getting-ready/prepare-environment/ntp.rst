Enable NTP on the Cluster and on the Browser Host
=================================================

The clocks of all the nodes in your cluster and the machine that runs the browser through which you access the Ambari Web interface must be able to synchronize with each other.

To check that the NTP service will be automatically started upon boot, run the following command on each host:

* **RHEL/CentOS 6**
  ::

    chkconfig --list ntpd

* **RHEL/CentOS 7**
  ::

    systemctl is-enabled ntpd


To set the NTP service to auto-start on boot, run the following command on each host:

* **RHEL/CentOS 6**
  ::

    chkconfig ntpd on

* **RHEL/CentOS 7**
  ::

    systemctl enable ntpd


To start the NTP service, run the following command on each host:

* **RHEL/CentOS 6**
  ::

    service ntpd start

* **RHEL/CentOS 7**
  ::

    systemctl start ntpd