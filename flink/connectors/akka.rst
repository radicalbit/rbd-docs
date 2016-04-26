===============
Akka Connector
===============

Introduction
------------

This connector provides sinks that writes data into a Cassandra database.

To use this connector, add the following dependency to your project:

.. remote-code-block:: xml
     main-repo
     pom.xml
    :caption: Xml
    :lines: 114-118
    :name: pom.xml

Note that the streaming connectors are currently not part of the binary distribution. See how to link with them for cluster execution `here <https://ci.apache.org/projects/flink/flink-docs-release-1.0/apis/cluster_execution.html#linking-with-modules-not-contained-in-the-binary-distribution>`_.

Akka Sink
--------------
