Tuning Ambari Performance
=========================

For clusters larger than 200 nodes, consider the following tuning options:

1. Calculate the new, larger cache size, using the following relationship:

  ::

    ecCacheSizeValue=60*<cluster_size>

  where ``<cluster_size>`` is the number of nodes in the cluster.

2. On the Ambari Server host, in ``/etc/ambari-server/conf/ambari-properties``, add the following property and value:

  ::

    server.ecCacheSize=<ecCacheSizeValue>

  where ``<ecCacheSizeValue>`` is the value calculated previously, based on the number of nodes in the cluster.

3. Add the following properties to adjust the JDBC connection pool settings:

  ::

    server.jdbc.connection-pool.acquisition-size=5
    server.jdbc.connection-pool.max-age=0
    server.jdbc.connection-pool.max-idle-time=14400
    server.jdbc.connection-pool.max-idle-time-excess=0
    server.jdbc.connection-pool.idle-test-interval=7200

4. If using MySQL as the Ambari database, in your MySQL configuration, increase the wait_timeout and interacitve_timeout to 8 hours (28800) and max. connections from 32 to 128.

  .. Important::
    It is critical that the Ambari configuration for ``server.jdbc.connection-pool.max-idle-time`` and ``server.jdbc.connection-pool.idle-test-interval`` must be lower than the MySQL ``wait_timeout and interactive_timeout`` set on the MySQL side. If you choose to decrease these timeout values, adjust`` downserver.jdbc.connection-pool.max-idle-time`` and ``server.jdbc.connection-pool.idle-test-interval`` accordingly in the Ambari configuration so that they are less than wait_timeout and interactive_timeout.

5. Restart Ambari Server.

  ::

    ambari-server restart
