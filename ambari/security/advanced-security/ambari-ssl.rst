Optional: Set Up SSL for Ambari
===============================

If you want to limit access to the Ambari Server to HTTPS connections, you need to provide a certificate.
While it is possible to use a self-signed certificate for initial trials, they are not suitable for production environments.
After your certificate is in place, you must run a special setup command.

Ambari Server should not be running when you do this. Either make these changes before you start Ambari the first time, or bring the server down before running the setup command.

1. Log into the Ambari Server host.

2. Locate your certificate. If you want to create a temporary self-signed certificate, use this as an example:

  ::

    openssl genrsa -out $wserver.key 2048
    openssl req -new -key $wserver.key -out $wserver.csr
    openssl x509 -req -days 365 -in $wserver.csr -signkey $wserver.key -out $wserver.crt

  Where ``$wserver`` is the Ambari Server host name.
  The certificate you use must be PEM-encoded, not DER-encoded. If you attempt to use a DER-encoded certificate, you see the following error:

  ::

    unable to load certificate 140109766494024:error:0906D06C:PEM routines:PEM_read_bio:no start line:pem_lib.c :698:Expecting: TRUSTED CERTIFICATE

  You can convert a DER-encoded certificate to a PEM-encoded certificate using the following command:

  ::

    openssl x509 -in cert.crt -inform der -outform pem -out cert.pem

  where ``cert.crt`` is the DER-encoded certificate and cert.pem is the resulting PEM-encoded certificate.

3. Run the special setup command and answer the prompts.

  ::

    ambari-server setup-security

  * Select ``1`` for ``Enable HTTPS for Ambari server.``
  * Respond ``y`` to ``Do you want to configure HTTPS ?``
  * Select the port you want to use for SSL. The default port number is 8443.
  * Provide the complete path to your certificate file (``$wserver.crt`` from above) and private key file (``$wserver.key`` from above).
  * Provide the password for the private key.
  * Start or restart the Server

    ::

      ambari-server restart

4. Trust Store Setup - If you plan to use Ambari Views with your Ambari Server, after enabling SSL for Ambari using the instructions below, you must also configure a Truststore for the Ambari Server. Refer to :doc:`Set Up Truststore for Ambari Server<ambari-server-truststore>` for more information.
