Optional: Configure Ciphers and Protocols for Ambari Server
===========================================================

1. Ambari provides control of ciphers and protocols that are exposed via Ambari Server.

To disable specific ciphers, you can optionally add a list of the following format to ambari.properties. If you specify multiple ciphers, separate each cipher using a vertical bar ``|``.

::

  security.server.disabled.ciphers=TLS_ECDHE_RSA_WITH_3DES_EDE_CBC_SHA

2. To disable specific protocols, you can optionally add a list of the following format to ambari.properties. If you specify multiple protocols, separate each protocol using a vertical bar ``|``.

::

  security.server.disabled.protocols=SSL|SSLv2|SSLv3