====================
Cassandra Connector
====================

Introduction
------------

This connector provides sinks that writes data into a Cassandra database.

The `official documentation <https://ci.apache.org/projects/flink/flink-docs-release-1.1/apis/streaming/connectors/cassandra.html>`_ contains in-depth details on the high level of interoperability between Cassandra and Flink.

To use this connector, add the following dependency to your project:

.. literalinclude:: /rbd-examples/flink/cassandra-connector-example/pom.xml
    :caption: pom.xml
    :name: cassandra-connector-example/pom.xml
    :language: xml
    :lines: 89-93
    :dedent: 2

Installing Apache Cassandra
----------------------------

Follow the instructions from the Cassandra Getting Started page.

Cassandra Sink
--------------

Flink's Cassandra sink are created by using the static ``CassandraSink.addSink(DataStream input)`` method. This method returns a ``CassandraSinkBuilder``, which offers methods to further configure the sink.

The following configuration methods can be used:

1. ``setQuery(String query)`` sets the query that is executed for every value the sink receives
2. ``setHost(String host[, int port])`` sets the cassandra host/port to connect to. This method is intended for simple use-cases. 
3. ``setClusterBuilder(ClusterBuilder builder)`` sets the cluster builder that is used to configure the connection to cassandra. The ``setHost()`` functionality can be subsumed with this method.
4. ``enableWriteAheadLog([CheckpointCommitter committer])`` is an optional method, that allows exactly-once processing for non-deterministic algorithms. A checkpoint committer stores additional information about completed checkpoints in some resource. This information is used to prevent a full replay of the last completed checkpoint in case of a failure. You can use a ``CassandraCommitter`` to store these in a separate table in cassandra.

  .. Note::
     This table will not be cleaned up by Flink.

5. ``build()`` finalize the configuration and returns the CassandraSink

Flink can provide exactly-once guarantees if the query is idempotent (meaning it can be applied multiple times without changing the result) and checkpointing is enabled. In case of a failure the failed checkpoint will be replayed completely.

Furthermore, for non-deterministic programs the write-ahead log has to be enabled. For such a program the replayed checkpoint may be completely different than the previous attempt, which may leave the database in an inconsitent state since part of the first attempt may already be written. The write-ahead log guarantees that the replayed checkpoint is identical to the first attempt. Note that that enabling this feature will have an adverse impact on latency.

.. literalinclude:: /rbd-examples/flink/cassandra-connector-example/src/main/java/io/radicalbit/CassandraConnectorExample.java
    :caption: CassandraConnectorExample
    :language: java 
    :name: CassandraConnectorExample
