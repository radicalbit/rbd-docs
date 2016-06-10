Client-to-node encryption
=========================

Enabling a Java client
----------------------

This section describes how to enable a Java client to work with a Cassandra cluster using SSL to encrypt communication.
To make client-to-node encryption, Java client will need a trustStore that includes the CA Root Certificate generated in the previous steps.

1. Generate a trustStore named :file:`client.jks` including the CA root certificate. Run:

   .. literalinclude:: /rbd-examples/snippets/cassandra-ssl/java-client-truststore-generation.txt
       :language: text

   Put the file in the classpath of the Java application. If using Maven convention, :file:`src/main/resources` folder could be a proper choice.

2. To enable client encryption on the server side, change the ``client_encryption_options`` section of |casYamlPath| for every node of the cluster as follows:

   .. literalinclude:: /rbd-examples/snippets/cassandra-ssl/cassandra-node-client-encryption-section.yaml
       :language: text

3. In Java client program, call the :code:`withSSL()` method when using the Cluster builder:

   .. literalinclude:: /rbd-examples/snippets/cassandra-ssl/cassandra-java-client-cluster-with-ssl.txt
       :language: java

4. Pass the trustStore location and password as Java parameters when starting the client:

   .. literalinclude:: /rbd-examples/snippets/cassandra-ssl/java-client-parameters.txt
       :language: text

   To pass trustStore programmatically change cluster building as this `example <https://github.com/radicalbit/cassandra-ssl-client-to-node-example/blob/master/src/main/java/io/radicalbit/cassandra/ClientToNode.java#L67>`_.


If something goes wrong, debug the SSL handshake adding :code:`-Djavax.net.debug=ssl` to program invokation.

Enabling cqlsh
--------------

After client authentication is enabled on nodes, |cqlsh| needs to be proper configured.

1. Convert the node certificate to the |pkcs12| format:

   .. literalinclude:: /rbd-examples/snippets/cassandra-ssl/jks-to-p12.txt
       :language: text

2. Convert the :file:`node1.p12` file to PEM format.

   .. literalinclude:: /rbd-examples/snippets/cassandra-ssl/p12-to-pem.txt
       :language: text

   Pay attention that ``-nodes`` option means *no DES*, so private key won't be encrypted.

3. Copy the file :file:`node1.pem` to the folder :file:`~/.cassandra` of the machine used to run |cqlsh|.

4. Edit (or create if not exists) a file named :file:`cqlshrc` in :file:`~/.cassandra` as follows.

   .. literalinclude:: /rbd-examples/snippets/cassandra-ssl/cqlshrc
       :language: text

   Put proper IP address of *node1*.

Repeat the procedure for the other nodes.











