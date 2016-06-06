Optional: Set Up Kerberos for Ambari Server
===========================================

When a cluster is enabled for Kerberos, the component REST endpoints (such as the YARN ATS component) require :doc:`SPNEGO</ambari/security/spnego>` authentication.

Depending on the Services in your cluster, Ambari Web needs access to these APIs.
Therefore, the Ambari Server requires a Kerberos principal in order to authenticate via SPNEGO against these APIs.
This section describes how to configure Ambari Server with a Kerberos principal and keytab to allow views to authenticate via SPNEGO against cluster components.

1. Create a principal in your KDC for the Ambari Server. For example, using kadmin:

  ::

    addprinc -randkey ambari-server@EXAMPLE.COM

2. Generate a keytab for that principal:

  ::

    xst -k ambari.server.keytab ambari-server@EXAMPLE.COM

3. Place that keytab on the Ambari Server host. Be sure to set the file permissions so the user running the Ambari Server daemon can access the keytab file.

  ::

    /etc/security/keytabs/ambari.server.keytab

4. Stop the ambari server.

  ::

    ambari-server stop

5. Run the setup-security command.

  ::

    ambari-server setup-security

6. Select 3 for Setup Ambari kerberos JAAS configuration.

7. Enter the Kerberos principal name for the Ambari Server you set up earlier.

8. Enter the path to the keytab for the Ambari principal.

9. Restart Ambari Server.

  ::

    ambari-server restart