Node-to-node encryption
=======================

To secure node-to-node communication, a Cassandra node will open secure sockets with other nodes **and** attempt
to identify other node requesting the connection (with Client Certificate Authentication).
This will avoid a fake node joining the cluster without the trust of the other nodes. The encryption and the authentication will work using a
`Public key infrastructure <https://en.wikipedia.org/wiki/Public_key_infrastructure>`_.

Before describing how to secure internode communication it's useful to recall what are *keyStore* and *trustStore* in the Java context.
During a SSL handshake, trustStore is used to verify credentials, while keyStore is used to provide credentials:

  * KeyStore holds private key and certificates and it is used when program is a SSL Server or SSL counterpart requires client authentication;
  * TrustStore holds certificates from a third party called Certificate Authority (CA). Both parts of the handshake trust the CA.

To simplify Cassandra setup, a specific Certificate Authority will be created.

Create a Certificate Authority
------------------------------

The first step is to generate a own |sslCA| with a Root Certificate. The Root Certificate will be used to sign other certificates.
OpenSSL will be used to create the CA. To simplify the workflow it's better to prepare a file with the configuration for the CA like the one below.

.. literalinclude:: /rbp-docs-code/snippets/cassandra-ssl/ca_generation.conf
    :language: text
    :caption: ca.conf

Run :code:`openssl req -config ca.conf -new -x509 -keyout ca.key -out ca.rootcertificate -days 365` to generate:

  * a new key for the CA (`ca.key`),
  * its Root Certificate (`ca.rootcertificate`) of type `PKCS#10 X.509`.

To verify the output run :code:`openssl x509 -in ca.rootcertificate -text -noout`.

Create node certificate
-----------------------

To provide encryption and authentication, every node will need a public/private key pair. To generate the pair, the ``keytool``
utility included in the JDK will be used. This command will generate the pair using a specific algorithm and will store it into
the provided keystore. If it does not exist, will be generated.

For every node run ``keytool`` with the ``genkeypair`` command as follows:

.. literalinclude:: /rbp-docs-code/snippets/cassandra-ssl/keytool-rsa-generation.txt
    :language: text

Pay attention to use the *same password* for ``keypass`` and ``storepass`` parameters due to a Cassandra limitation. Repeat the procedure for
*node2*, *node3* and so on changing node name. To complete description of the command, the list of parameters applied

  * ``keyalg``, the RSA algorithm is used,
  * ``keysize``, is the size of the key to generate,
  * ``keypass``, is the password for the key,
  * ``alias``, is a mnemonic name for the pair,
  * ``keystore``, the filename of the keystore,
  * ``storepass`` is the password of the generated keystore,
  * ``validity`` is the number of days of validity for the key pair,
  * ``dname`` is the distinguished name relative to your company.

To verify the output run :code:`keytool -list -v -keystore node1.jks -storepass N0dePa$$word`

Sign node certificate with CA
-----------------------------

In order to get trusted, node certificates need to be signed by the CA. This is done into two steps:
  1. every node must export a *Certificate Sign Request* corresponding to the previously created certificate
  2. the CSR must be signed by the CA

To export the CSR for alias ``node1`` stored in the :file:`node1.jks` file run :code:`keytool` with the :code:`certreq` command:

.. literalinclude:: /rbp-docs-code/snippets/cassandra-ssl/keytool-csr-generation.txt
    :language: text

This command will extract the CSR into the file :file:`node1.csr`.

To sign the CSR run the command:

.. literalinclude:: /rbp-docs-code/snippets/cassandra-ssl/openssl-csr-sign.txt
    :language: text

This will generate a CA signed certificate into the file :file:`node1.sc` using the CSR created in the previous step with a validity of 365 days.
The ``CA`` and ``CAkey`` parameters are those files written when creating the CA Authority. The ``passin`` parameter allows to input a password.
In this case password is provided inside command with the :code:`pass:` prefix. Other methods are available at `official doc <https://www.openssl.org/docs/manmaster/apps/openssl.html#PASS-PHRASE-ARGUMENTS>`_.

Repeat the procedure for the another nodes using proper files [#]_.


Import signed certificate
-------------------------

Signed certificate need to be imported back into the keystore, this will allow node to authenticate against the others.
To properly do this, first import the CA Root Certificate. This will create a correct chain of trust.
To import the signed certificate for :file:`node1` run:

.. literalinclude:: /rbp-docs-code/snippets/cassandra-ssl/import-caroot.txt
    :language: text

After this, import back the signed certificate for file:`node1` into its keystore using the same alias.

.. literalinclude::  /rbp-docs-code/snippets/cassandra-ssl/import-signed-certificate.txt
    :language: text

Once again, to verify the output run :code:`keytool -list -v -keystore node1.jks -storepass N0dePa$$word`
Repeat the procedure for the another nodes using proper keystore.

Create the trustStore
---------------------

Every node will trust the |sslCA| as long as its certificate is in the trustStore. To create the trustStore and insert the Root Certificate, run this command:

.. literalinclude:: /rbp-docs-code/snippets/cassandra-ssl/create-trust-store.txt
    :language: text


Configure Cassandra node
------------------------

For every node, do the following steps:

  1. Copy proper keyStore to |casConfDir| folder renaming it as :file:`keystore.jks`. For example for node 1, copy :file:`node1.jks` to :file:`$CASSANDRA_HOME/conf/keystore.jks`.
     Do the same for the trustStore copying the file :file:`truststore.jks` under |casConfDir|.

  2. Replace ``server_encryption_options`` of |casYamlPath| with the following snippet. Specify the full path of keyStore and trustStore.

     .. literalinclude:: /rbp-docs-code/snippets/cassandra-ssl/security-cassandra-yaml.txt
         :language: text

   3. Download *Java Cryptography Extension (JCE) Unlimited Strength Jurisdiction Policy Files for JDK/JRE 7*
      from `Oracle site <http://www.oracle.com/technetwork/java/javase/downloads/jce-7-download-432124.html>`_, unzip and copy it
      under ``${JAVA_HOME}/jre/lib/security/`` This will allow to use `strong encryption with 256bit AES <https://en.wikipedia.org/wiki/Advanced_Encryption_Standard>`_.

   4. Restart the node.


Debugging
---------

In case of problems, it's possible to debug SSL handshake adding :code:`-Djavax.net.debug=ssl` to |casEnvSh|.
This `guide <http://docs.oracle.com/javase/7/docs/technotes/guides/security/jsse/ReadDebug.html>`_ explains how to read the debug output.





.. [#] Use the ``-CAcreateserial`` option the first time the CA is used to sign a certificate. This option will create the ``ca.srl`` file containing a serial number. Next time the CA is used to sign, use instead the ``-CAserial ca.srl`` option and no more ``-CAcreateserial``. This file will be incremented each time a new certificate is signed. The serial number will be readable once the certificate is imported to a |pkcs12| format.








