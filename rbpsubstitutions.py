versions_subs="""
.. |alluxio-version| replace:: 1.0.1
.. |kafka-version| replace:: 0.10.0.1
.. |kafka-connector-version| replace:: 0.10
.. |cassandra-version| replace:: 2.2.5
.. |ambari-version| replace:: 2.2.0
.. |flink-version| replace:: 1.1.1
"""

other_substitutions="""
.. |fdd| replace:: Radicalbit Distribution
"""

alluxio_subs="""
.. |ufs| replace:: under file system
.. |uss| replace:: underlying storage system
"""

ssl_subs="""
.. |sslCA| replace:: Certificate Authority (CA)
.. |sslOpen| replace:: ``openssl``
.. |pkcs12| replace:: ``PKCS#12``
"""

cassandra_subs="""
.. |cqlsh| replace:: ``cqlsh``
.. |casLibDir| replace:: ``$CASSANDRA_HOME/lib``
.. |casConfDir| replace:: ``$CASSANDRA_HOME/conf``
.. |casBinDir| replace:: ``$CASSANDRA_HOME/bin``
.. |casStartSh| replace:: ``$CASSANDRA_HOME/bin/cassandra.in.sh``
.. |casYamlPath| replace:: ``$CASSANDRA_HOME/conf/cassandra.yaml``
.. |casEnvSh| replace:: ``$CASSANDRA_HOME/bin/cassandra-env.sh``
.. |casKrbConf| replace:: ``kerberos.conf``
"""

ambari_subs="""
.. |rbd-stack| replace:: RBD
.. |rbd-version| replace:: 1.0
"""

all_substitutions=versions_subs+other_substitutions+cassandra_subs+ssl_subs+ambari_subs+alluxio_subs
