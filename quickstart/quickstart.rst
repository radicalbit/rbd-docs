**********************************
How to create your first Flink Job
**********************************

This tutorial will guide you through the basic steps to create a simple Flink job, include optional dependency to integrate with other components, build a JAR and submit it to a running Flink session.

===================
Create your project
===================

The first step required is to use our Maven archetype to create a new project.
    

.. literalinclude:: /rbd-examples/snippets/mvn-archetype-java.rst 
    :language: text
    :caption: Java

.. literalinclude:: /rbd-examples/snippets/mvn-archetype-scala.rst
    :caption: Scala
    :language: text

This operation will create a folder structure together with a :file:`pom.xml` file designed to properly import Flink dependencies and to build a JAR in the most efficient way. 


A simple Flink Job
==================

Now we can go through a simple Flink Job that will introduce you to the basic structure of a Flink Job. Here is an example of a Job that takes a stream of strings as an input, process them and then prints them to console.

.. literalinclude:: /rbd-examples/mvn/src/main/java/radicalbit/io/java/QuickstartFirstJob.java
    :language: java
    :caption: Java
    :name: quick-java

.. literalinclude:: /rbd-examples/mvn/src/main/scala/radicalbit/io/scala/QuickstartFirstJob.scala
    :language: scala
    :caption: Scala
    :name: quick-scala

The `Flink Programming guide <https://ci.apache.org/projects/flink/flink-docs-release-1.1/>`_ provides a good resource to start learning how to develop on Flink, giving examples and explanations of the many high-level abstractions used by the framework. If this is the first time you work with Flink, there you will find all the required fundamentals to work with it.


Build, pack and submit your application
=======================================

The advised mode to run your application on Flink is to submit a JAR to a running Flink session managed through Ambari interface. To package your application, simply go to the root folder of your project and call

::

  mvn clean package

=================
Kafka Integration
=================

To include a Kafka Source or a Kafka Sink into your program you will first need to include the dependency in your :file:`pom.xml` file. The package :file:`kafka-connector` includes all that is necessary to connect a streaming job to Kafka, to process and publish on a Kafka topic.


.. literalinclude:: /rbd-examples/snippets/include-kafka.xml
    :language: xml
    
.. NOTE::
   RBD-Antelao distributes only Kafka |kafka-version| and therefore you are advised to use exclusively the one built for Kafka |kafka-connector-version|. 

To discover how to actually use this connector, please refer to the following document: :doc:`../flink/connectors/kafka`.

.. _alluxio-hadoop-interface:

==================================
Read and Write from and to Alluxio
==================================

Alluxio can be used as any other \*nix filesystem and Flink allows you to use it as an ordinary filesystem. To write and read from and to Alluxio it is enough to prepend the dedicated file scheme :file:`alluxio://` to the path.  


.. literalinclude:: /rbd-examples/snippets/alluxio-example.rst
	:language: java

.. NOTE::
   RBD-Antelao defines Alluxio as the default filesystem so the `alluxio://` scheme is optional and if no scheme is specified, Flink will perform operations on Alluxio.

=============================
Cassandra Database connection
=============================

Flink offers a dedicated `CassandraInputFormat` and `CassandraOutputFormat` to be used to read and write data in batch mode and to write data in streaming mode. These classes are included in the :file:`connector-cassandra` package and you will need to add it to the dependencies in your :file:`pom.xml` file.

.. literalinclude:: /rbd-examples/snippets/include-cassandra.xml
	:language: xml

For a more detailed guide to use the Cassandra Connectors, please refer to the OMISSIS.

