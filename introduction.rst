============
Introduction
============

Rationale
---------

The Radicalbit Fast Data Distribution (RBFDD) is a collection of Open Source (`ASL 2.0-licenced <https://www.apache.org/licenses/LICENSE-2.0.html>`_) software products connecting, leveraging and exploiting data, network, intelligence and computing power.

RBFDD includes modern, present and future-proof technologies, fully integrated, forming an end-to-end data pipeline computing environment in which a pool of software, leveraging computers collaborating over the network, takes part to solve complex problems in order to achieve a common goal.

RBFDD is a seamlessly integrated computing layer enabling organizations to develop and run business logic such as:

* statistical analysis
* predictive and prescriptive analysis
* log analytics
* anomaly detection
* smart metering
* fraud detection
* anti-money laundering
* graph processing
* industrial internet (IoT)
* any analytics task requiring speed at scale

in a fast, event-driven, scalable, resilient, secure, highly available and integrated environment.

RBFDD supports both batch, long-running jobs, and streaming, pure real-time processing, leveraging concepts such as parallel, distributed, and in-memory computing in order to process massive amount of data and workload at speed.

RBFDD acts as a computing layer, service or ingestion at your will, providing organizations the ability to develop, integrate and deploy services requiring complex calculations, data intensive computation or real-time processing.

RBFDD allows implementing data-driven, service-oriented systems, by quickly get up and running with one of the most advanced piece of software technology currently available on the market.

Components overview
-------------------

The following diagram displays the ecosystem of software components in which RBFDD lives; in blue are components part of the distribution, while in green are key components that, while not being provided along with the distribution, represent a key feature item for which integrations (across several dimensions) are provided, or that are otherwise regarded as a first-class citizen in the distribution:

.. image:: /img/introduction/blueprint.svg
   :height: 400px
   :width: 640px
   :alt: RBFDD Blueprint
   :align: center

.

Ambari
------

`Apache Ambari <https://ambari.apache.org/>`_ is a completely Open Source management platform to provision, manage, monitor and secure Apache Hadoop clusters. Apache Ambari takes the guesswork out of operating Hadoop.

Motivation
~~~~~~~~~~

* Need to collect metrics about each component for monitoring and alerting purposes
* Need a solution to include and deploy everything necessary to set up the service
* Need for a solution to dynamically manage service life-cycle (start, stop and restart) and scalability

Features
~~~~~~~~

* Provisioning
* Management
* Monitoring
* Security
* Broad product integration
* Broad OS integration

Kafka
-----

`Apache Kafka <https://kafka.apache.org/>`_ is a high-throughput, distributed, publish-subscribe messaging system rethought as a distributed commit log.

Motivation
~~~~~~~~~~

* Need to integrate with one of the most known messaging system used for applications such as web activity tracking, operational metrics, log aggregation and stream processing

Features
~~~~~~~~

* Fast
* Scalable
* Durable
* Distributed by design

Akka
----

`Akka <http://akka.io>`_ is a toolkit and runtime for building highly concurrent, distributed, and resilient message-driven applications on the JVM.

Motivation
~~~~~~~~~~

* Need to integrate with one of the most known toolkit used for developing `Reactive Systems <https://reactivemanifesto.org/>`_:

  * Responsive, 
  * Elastic, 
  * Resilient and 
  * Event-Driven

Features
~~~~~~~~

* Simple concurrency and distribution
* Resilient by design
* High performance
* Elastic and decentralized
* Extensible

Flink
-----

`Apache Flink <https://flink.apache.org/>`_ is an Open Source framework for "Fast Data" analytics. It builds on top of a sophisticated, performant and resilient distributed stream processing engine, allowing both batch and real-time streaming workflows to be defined with an intuitive API.

Apart from the DataSet (batch) and DataStream (streaming) APIs, Flink also provides more task-specific APIs:

* the Table API allows to express workflows in a SQL-like fashion, embedded in either Java or Scala projects
* FlinkML is a library that enables to apply machine learning algorithms to huge data sets
* Gelly is a graph processing API and library
* Flink CEP is a "complex event processing" API that allows to detect and react to occurrences of event patterns in a stream

Motivation
~~~~~~~~~~

* Many applications require cyclic streams (parallel model training, evaluation)
* Many applications require real-time true streaming

Features
~~~~~~~~

* High performance, low latency
* Support for event time and out-of-order events
* Exactly-once semantics for stateful computations
* Highly flexible streaming windows
* Continuous streaming model with backpressure
* Fault tolerance via lightweight distributed snapshots
* A unified runtime systems for batch and stream processing
* Built-in memory management
* Native support for iterations and delta iterations
* Lazy DAG evaluation with a sophisticated optimization engine
* Rich library ecosystem
* Broad integration with other software products in the "Big Data"/Hadoop ecosystem

Alluxio
-------

`Alluxio <http://alluxio.org/>`_ is a memory-speed virtual distributed storage system.

Motivation
~~~~~~~~~~

* Need to leverage memory processing
* Need to share context among different jobs
* Need for fault tolerance among different jobs

Features
~~~~~~~~

* Context sharing across (heterogeneous) jobs
* Lineage: reliable file sharing without replication

  * One copy of data in memory (fast)
  * Upon failure, re-compute data using lineage (fault tolerant)

* Flexible tiered storage: leverage memory, SSDs or HDDs according to your needs (fine tune speed and capacity requirements)

  * Pluggable data management policy (promote hot data to upper tiers, evict cold data to lower tiers)
  * Transparent naming across several distributed filesystems

* Unified namespace

  * Transparent naming across several distributed file systems
  * Shared data across heterogeneous storage systems
  * Mount/unmount on-the-fly

Cassandra
---------

`Apache Cassandra <https://cassandra.apache.org>`_ is an Open Source distributed database management system designed to handle large amounts of data across many commodity servers, providing high availability with no single point of failure.

Motivation
~~~~~~~~~~

* Need to integrate a highly available and performing column oriented data store to support a more flexible data model
* Need to integrate a store, which could be used for real-time and time series analytics

Features
~~~~~~~~

* Peer-to-peer architecture, highly available design with no single point of failure
* No shared storage requirements for failover
* Simple deployment and maintenance
* Multi-datacenter support
* Hadoop-compatible
* File-append support
* Multiple file systems
* Tuneable data locality
* Small files optimization
* Per-file segment and block size support
* Sequential and random access to file support
* Security: native authentication, Kerberos support
* File watcher notification service
* Compression
* Encryption

Zeppelin
--------

`Apache Zeppelin <https://zeppelin.apache.org/>`_ is a web-based notebook that enables interactive data analytics.

Motivation
~~~~~~~~~~

* Need for tool for data exploration and discovery
* Need for a fast prototyping tool

Features
~~~~~~~~

* Data exploration
* Data discovery
* Data analytics
* Data visualization
* Collaboration platform
* Security integration
