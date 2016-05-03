versions_subs="""
.. |kafka-version| replace:: 0.9.0.1
.. |kafka-connector-version| replace:: 0.9
.. |cassandra-version| replace:: 2.2.5
"""

other_substitutions="""
.. |fdd| replace:: Radicalbit Fast Data Distribution
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


all_substitutions=versions_subs+other_substitutions+cassandra_subs+ssl_subs

