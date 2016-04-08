**********************************************
How to start developing on Radicalbit Platform
********************************************** 


This tutorial will guide you through the basic steps to create a simple Flink job, include optional dependency to integrate with other components, build a JAR and submit it to a running Flink session.

===================
Create your project
===================

The first step required is to use our Maven archetype to create a new project.
    

.. remote-code-block:: xml 
    snippet-repo 
    mvn-archetype-java.rst 
    :caption: Java

.. remote-code-block:: xml
    snippet-repo 
    mvn-archetype-scala.rst
    :caption: Scala

This operation will create a folder structure together with a :file:`pom.xml` file designed to properly import Flink dependencies and to build a JAR in the most efficient way. With this you should be able to create an executable Flink program. Let's see a simple example:

.. remote-code-block:: java
    java-repo 
    QuickstartFirstProgram.java
    :caption: Java

.. literalinclude:: code/scala-first-program.rst
	:caption: Scala

=======================================
Build, pack and submit your application
=======================================

The advised mode to run your application on Flink is to submit a JAR to a running Flink session managed through Ambari interface. To package your application, simply go to the root folder of your project and call

::

  mvn clean package

=================
Kafka Integration
=================

To include a Kafka Source or a Kafka Sink into your program you will first need to include the dependency in your :file:`pom.xml` file. The package :file:`kafka-connector` includes all that is necessary to connect a streaming job to Kafka, to process and publish on a Kafka topic.


.. remote-code-block:: xml
    snippet-repo 
    include-kafka.xml
    
.. NOTE::
   RBP-Antelao distributes only Kafka |kafka-version| and therefore you are advised to use exclusively the one built for Kafka |kafka-connector-version|. 

To discover how to actually use these connector, please refer to the OMISSIS.

==================================
Read and Write from and to Alluxio
==================================

Alluxio can be used as any other \*nix filesystem and Flink allows you to use it as an ordinary filesystem. To write and read from and to Alluxio it is enough to prepend the dedicated file scheme :file:`alluxio://` to the path.  


.. remote-code-block:: java
    snippet-repo 
    alluxio-example.rst

.. NOTE::
   RBP-Antelao defines Alluxio as the default filesystem so the `alluxio://` scheme is optional and if no scheme is specified, Flink will perform operations on Alluxio.

=============================
Cassandra Database connection
=============================

Flink offers a dedicated `CassandraInputFormat` and `CassandraOutputFormat` to be used to read and write data in batch mode and to write data in streaming mode. These classes are included in the :file:`connector-cassandra` package and you will need to add it to the dependencies in your :file:`pom.xml` file.

.. remote-code-block:: xml
    snippet-repo 
    include-cassandra.xml

For a more detailed guide to use the Cassandra Connectors, please refer to the OMISSIS.

