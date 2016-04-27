===============
Akka Connector
===============
<<<<<<< HEAD

Introduction
------------

This connector provides sink that sends data to a remote actor.

To use this connector, add the following dependency to your project:

.. literalinclude:: /rbp-docs-code/pom.xml 
    :caption: pom.xml
    :language: xml
    :lines: 119-123
    :name: pom-akka.xml

Note that the streaming connectors are currently not part of the binary distribution. See how to link with them for cluster execution `here <https://ci.apache.org/projects/flink/flink-docs-release-1.0/apis/cluster_execution.html#linking-with-modules-not-contained-in-the-binary-distribution>`_.

Akka Sink
----------

The ``AkkaSink`` is used for sending data from a Flink stream to a remote actor. Note that the sink is not involved in any exactly-once process, in case of failure data will be sent again to remote actor; its behaviour is called "at-least-once".

The AkkaSink expected the following arguments:

1. systemName (Optional): It's the name of the underlying Actor System that it manages the connection between the job and the remote actor.
2. path: address of the remote actor example. ``akka.tcp://system-remote@ip:port/user/remote-actor``
3. conf: Sequence of akka configuration. At the moment the sink have to create a dedicated ActorSystem for each task. So it is mandatory to provide a number of configurations equals to the number of parallelism.

Example
--------

.. literalinclude:: /rbp-docs-code/src/main/scala/radicalbit/io/scala/AkkaReceiverExample.scala
   :caption: AkkaReceiverExample
   :language: scala
   :name: AkkaReceiverExample

.. literalinclude:: /rbp-docs-code/src/main/scala/radicalbit/io/scala/AkkaSinkExample.scala
   :caption: AkkaSinkExample
   :language: scala
   :name: AkkaSinkExample

=======
>>>>>>> b8122eb147491ffeb90c62df31199fe835d0722e
