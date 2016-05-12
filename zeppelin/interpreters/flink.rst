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

How to configure interpreter to point to Flink cluster
-------------------------------------------------------
At the "Interpreters" menu, you have to create a new Flink interpreter and provide next properties:

+----------------+--------------------------+--------------------------------------------------------------+
|property        | value (example)          |  Description                                                 |
+----------------+--------------------------+--------------------------------------------------------------+
|host            | yarn                     | - host name of running JobManager.                           |
|                |                          | - 'local' runs Flink in local mode (default)                 | 
|                |                          | - 'yarn' to attach the interpreter to a running YARN cluster |
+----------------+--------------------------+--------------------------------------------------------------+
|port            | 6123                     |  Port of running JobManager, ignored by yarn mode            |
+----------------+--------------------------+--------------------------------------------------------------+
|flink.conf.dir  | /path/to/flink-conf.yaml |  Absolute path of flink-conf-yaml (optional)                 |
+----------------+--------------------------+--------------------------------------------------------------+
|flink.user      | user/runs/flink/service  |  User runs Flink's service (optional)                        |
+----------------+--------------------------+--------------------------------------------------------------+
Instead of using properties ``flink.conf.dir`` and ``flink-user``, you can use the environments variables ``FLINK_CONF_DIR`` and ``FLINK_USER``.

For more information about Flink configuration, see the official documentation `here <https://ci.apache.org/projects/flink/flink-docs-release-1.0/setup/config.html>`_.

Working with YARN
------------------
In order to connect the interpreter with an existing Flink YARN Cluster, configuration and user must be set because JobManager's host and port have provided by an internal Flink mechanism.
