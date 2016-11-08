==================
Flink Interpreter
==================

Flink interpreter for Apache Zeppelin
--------------------------------------

`Apache Flink <https://flink.apache.org/>`_ is an open source platform for distributed stream and batch data processing. Flink’s core is a streaming dataflow engine that provides data distribution, communication, and fault tolerance for distributed computations over data streams. Flink also builds batch processing on top of the streaming engine, overlaying native iteration support, managed memory, and program optimization.

How to start local Flink cluster, to test the interpreter
----------------------------------------------------------
Zeppelin comes with pre-configured flink-local interpreter, which starts Flink in a local mode on your machine, so you do not need to install anything.

Flink Interpreter allows you to run jobs, both batch and streaming, via browser to explore and prototyping on Datasets.

How to configure interpreter to point to the Flink cluster
----------------------------------------------------------
If you add the Flink service to the |fdd|, the Zeppelin interpreter will be automatically configured to work with it. No additional steps are required.
