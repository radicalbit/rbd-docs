Set Up Truststore for Ambari Server
===================================

If you plan to Set Up SSL for Ambari or to enable wire encryption for |rbd-stack|, you must configure the Truststore for Ambari and add certificates.

Ambari Server should not be running when you do this.
Either make these changes before you start Ambari the first time, or bring the server down before running the setup command.

1. On the Ambari Server, create a new keystore that will contain the Ambari Server's HTTPS certificate.

  ::

    keytool -import -file <path_to_the_Ambari_Server's_SSL_Certificate> \
      -alias ambari-server \
      -keystore ambari-server-truststore

  When prompted to ``Trust this certificate?`` type ``yes``.

2. Configure the ambari-server to use this new trust store:

  ::

    ambari-server setup-security
    Using python  /usr/bin/python2.6
    Security setup options...
    ===========================================================================
    Choose one of the following options:
    [1] Enable HTTPS for Ambari server.
    [2] Encrypt passwords stored in ambari.properties file.
    [3] Setup Ambari kerberos JAAS configuration.
    [4] Setup truststore.
    [5] Import certificate to truststore.
    ===========================================================================
    Enter choice, (1-5): *4*
    Do you want to configure a truststore [y/n] (y)? *y*
    TrustStore type [jks/jceks/pkcs12] (jks): *jks*
    Path to TrustStore file : *<path to the ambari-server-truststore keystore>*
    Password for TrustStore:
    Re-enter password:
    Ambari Server 'setup-security' completed successfully.

3. Once configured, the Ambari Server must be restarted for the change to take effect.

  ::

    ambari-server restart