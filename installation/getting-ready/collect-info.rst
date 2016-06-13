===================
Collect Information
===================

Before deploying an |rbd-stack| cluster, you should collect the following information:

* The fully qualified domain name (FQDN) of each host in your system. The Ambari install wizard supports using IP addresses. You can use ``hostname -f`` to check or verify the FQDN of a host.

.. Note::

    Deploying all |rbd-stack| components on a single host is possible, but is appropriate only for initial evaluation purposes. Typically, you set up at least three hosts; one master host and two slaves, as a minimum cluster.

* A list of components you want to set up on each host.
* The base directories you want to use as mount points for storing:

  * NameNode data
  * DataNodes data
  * Secondary NameNode data
  * Cassandra data
  * Alluxio data
  * ZooKeeper data, if you install ZooKeeper
  * Various log, pid, and db files, depending on your install type


.. Important::

    You must use base directories that provide persistent storage locations for your |rbd-stack| components and your Hadoop data. Installing |rbd-stack| components in locations that may be removed from a host may result in cluster failure or data loss. For example: Do Not use /tmp in a base directory path.