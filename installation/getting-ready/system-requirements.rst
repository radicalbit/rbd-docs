================================
Meet Minimum System Requirements
================================

To run |fdd|, your system must meet the following minimum requirements:


Operating Systems Requirements
______________________________

The following, 64-bit operating systems are supported:

* Red Hat Enterprise Linux (RHEL) v7.x
* Red Hat Enterprise Linux (RHEL) v6.x
* CentOS v7.x
* CentOS v6.x

.. Important::
  The installer pulls many packages from the base OS repositories. If you do not have a complete set of base OS repositories available to all your machines at the time of installation you may run into issues.

Browser Requirements
____________________

The Ambari Install Wizard runs as a browser-based Web application. You must have a machine capable of running a graphical browser to use this tool. The minimum required browser versions are:

* Windows (7, 8)

  * Internet Explorer 10
  * Firefox 18
  * Google Chrome 26

* Mac OS X (10.6 or later)

  * Firefox 18
  * Safari 5
  * Google Chrome 26

* Linux (CentOS, Debian, Oracle Linux, RHEL, SLES, Ubuntu)

  * Firefox 18
  * Google Chrome 26

On any platform, we recommend updating your browser to the latest, stable version.

Software Requirements
_____________________

On each of your hosts:

* yum and rpm (RHEL/CentOS)
* scp, curl, unzip, tar, and wget
* OpenSSL (v1.01, build 16 or later)
* Python

  * For CentOS 6: Python 2.6.*
  * For CentOS 7: Python 2.7.*

JDK Requirements
________________

The following Java runtime environments are supported:

* Oracle JDK 1.8 64-bit (minimum JDK 1.8_60) (default)
* Oracle JDK 1.7 64-bit (minimum JDK 1.7_67)
* OpenJDK 8 64-bit
* OpenJDK 7 64-bit

.. Note::

    JDK support is dependent on your choice of |rbd-stack| Stack. Refer to :doc:`Changing the JDK Version for more information</ambari/reference/change-jdk>`.

Database Requirements
_____________________

Ambari requires a relational database to store information about the cluster configuration and topology. The following list outlines all usable databases:

* PostgreSQL 8
* PostgreSQL 9.1.13+,9.3
* MySQL 5.6
* Oracle 11gr2, 12c

By default, Ambari will install an instance of PostgreSQL on the Ambari Server host. Optionally, to use an existing instance of PostgreSQL, MySQL or Oracle. For further information, see :doc:`Using Non-Default Databases</ambari/reference/non-default-db>`.

.. Important::

    For the Ambari database, if you use an existing Oracle database, make sure the Oracle listener runs on a port other than 8080 to avoid conflict with the default Ambari port. Alternatively, refer to the Ambari Reference Guide for information on :doc:`Changing the Default Ambari Server Port</ambari/reference/configuring-ports>`.

Memory Requirements
___________________

The Ambari host should have at least 1 GB RAM, with 500 MB free.

To check available memory on any host, run:

::

	free -m

If you plan to install the Ambari Metrics Service (AMS) into your cluster the host you plan to run the Ambari Metrics Collector host should have the following memory and disk space available based on cluster size:

+-----------------+------------------+------------+
| Number of hosts | Memory Available | Disk Space |
+=================+==================+============+
| 1               | 1,024 MB         | 10 GB      |
+-----------------+------------------+------------+
| 10              | 1,024 MB         | 20 GB      |
+-----------------+------------------+------------+
| 50              | 2,048 MB         | 50 GB      |
+-----------------+------------------+------------+
| 100             | 4,096 MB         | 100 GB     |
+-----------------+------------------+------------+
| 300             | 4,096 MB         | 100 GB     |
+-----------------+------------------+------------+
| 500             | 8,096 MB         | 200 GB     |
+-----------------+------------------+------------+
| 1,000           | 12,288 MB        | 200 GB     |
+-----------------+------------------+------------+
| 2,000           | 16,348 MB        | 500 GB     |
+-----------------+------------------+------------+


.. note::
  The above is offered as guidelines. Be sure to test for your particular environment. Also refer to :ref:`Package Size and Inode Count Requirements<ambari-inode-count>` for more information on package size and Inode counts.

.. _ambari-inode-count:

Package Size and Inode Count Requirements
_________________________________________

Size and Inode values are approximate

+----------------------------+----------+-----------+
|                            | Size     | Inodes    |
+============================+==========+===========+
| Ambari Server              | 100 MB   |     5,000 |
+----------------------------+----------+-----------+
| Ambari Agent               | 8 MB     |     1,000 |
+----------------------------+----------+-----------+
| Ambari Metrics Collector   | 225 MB   |     4,000 |
+----------------------------+----------+-----------+
| Ambari Metrics Monitor     | 1 MB     |       100 |
+----------------------------+----------+-----------+
| Ambari Metrics Hadoop Sink | 8 MB     |       100 |
+----------------------------+----------+-----------+
| After Ambari Server Setup  | N/A      |     4,000 |
+----------------------------+----------+-----------+
| After Ambari Server Start  | N/A      |       500 |
+----------------------------+----------+-----------+
| After Ambari Agent Start   | N/A      |       200 |
+----------------------------+----------+-----------+

Check the Maximum Open File Descriptors
_______________________________________

The recommended maximum number of open file descriptors is 10000, or more. To check the current value set for the maximum number of open file descriptors, execute the following shell commands on each host:

::

  ulimit -Sn
  ulimit -Hn


If the output is not greater than 10000, run the following command to set it to a suitable default:

::

	ulimit -n 10000