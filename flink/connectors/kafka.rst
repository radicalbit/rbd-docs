===============
Kafka Connector
===============

Introduction
------------

Due to its nature, the distributed publish/subscribe Apache Kafka is one of the best matches to read data from and write data to for Flink.

The `official documentation <https://ci.apache.org/projects/flink/flink-docs-release-1.0/apis/streaming/connectors/kafka.html>`_ contains in-depth details on the high level of interoperability between Kafka and Flink.

To use the connector, you should first of all include the following dependency in your project's POM:

.. literalinclude:: /rbp-docs-code/mvn/pom.xml
    :caption: pom.xml
    :language: xml
    :lines: 120-124

Security
--------

RBFDD includes a custom Flink version that allows the user to make the two systems interoperate even on *secure* clusters.

The feature is mostly transparent to the client code, the only required step is to add a property to the ``FlinkKafkaConsumer09`` and/or the ``FlinkKafkaProducer09``, this property being ``security.protocol``, whose value should be set to ``SASL_PLAINTEXT``.

.. Note::

    RBFDD ships with Kafka |kafka-version|, which supports Kerberos security. Please be advised that producers and consumers for previous versions of Kafka, despite being shipped along with Flink, *won't work* due to wire-protocol incompatibility. You should always use the aforementioned ``FlinkKafkaConsumer09`` and ``FlinkKafkaProducer09``.

The following program serves as an example of a trivial job using Kafka as both source and sink that can run on a secure cluster as well.

.. literalinclude:: /rbp-docs-code/flink/kafka-connector-example/src/main/scala/io/radicalbit/flink/examples/KafkaConnectorExample.scala
    :caption: KafkaExample.scala
    :language: scala
