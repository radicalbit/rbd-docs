Enabling SPNEGO Authentication for Hadoop
=========================================

By default, access to the HTTP-based services and UI’s for the cluster are not configured to require authentication.
Kerberos authentication can be configured for the Web UI for HDFS.

.. _ambari-configure-authenticated-http:

Configure Ambari Server for Authenticated HTTP
______________________________________________

In order for Ambari to work with a cluster in which authenticated HTTP access to the Web UI’s is required, you must configure the Ambari Server for Kerberos.
Refer to :doc:`Set Up Kerberos for Ambari Server for more information<advanced-security/ambari-server-kerberos>`.

Configuring HTTP Authentication for HDFS
_________________________________________________

1. Create a secret key used for signing authentication tokens.
This file should contain random data and be placed on every host in the cluster.
It should also be owned by the hdfs user and group owned by the rbp-services group.
Permissions should be set to 440. For example:

  ::

    dd if=/dev/urandom of=/etc/security/http_secret bs=1024 count=1
    chown hdfs:hadoop /etc/security/http_secret
    chmod 440 /etc/security/http_secret

2. In Ambari Web, browse to **Services > HDFS > Configs**.

3. Add or modify the following configuration properties to Advanced core-site.

  +-----------------------------------------------------+------------------------------------------------------------+
  | Property                                            | New Value                                                  |
  +=====================================================+============================================================+
  | hadoop.http.authentication.simple.anonymous.allowed | false                                                      |
  +-----------------------------------------------------+------------------------------------------------------------+
  | hadoop.http.authentication.signature.secret.file    | /etc/security/http_secret                                  |
  +-----------------------------------------------------+------------------------------------------------------------+
  | hadoop.http.authentication.type                     | kerberos                                                   |
  +-----------------------------------------------------+------------------------------------------------------------+
  | hadoop.http.authentication.kerberos.keytab          | /etc/security/keytabs/spnego.service.keytab                |
  +-----------------------------------------------------+------------------------------------------------------------+
  | hadoop.http.authentication.kerberos.principal       | **HTTP/_HOST@EXAMPLE.COM**                                 |
  +-----------------------------------------------------+------------------------------------------------------------+
  | hadoop.http.filter.initializers                     | org.apache.hadoop.security.AuthenticationFilterInitializer |
  +-----------------------------------------------------+------------------------------------------------------------+
  | hadoop.http.authentication.cookie.domain            | **yourdomain.local**                                       |
  +-----------------------------------------------------+------------------------------------------------------------+

  .. Note::
    The entries listed in the above table in **bold** and italicized are site-specific. The ``hadoop.http.authentication.cookie.domain`` property is based off of the fully qualified domain names of the servers in the cluster. For example if the FQDN of your NameNode is ``host1.yourdomain.local``, the ``hadoop.http.authentication.cookie.domain`` should be set to ``yourdomain.local``.

4. Save the configuration, then restart the affected services.