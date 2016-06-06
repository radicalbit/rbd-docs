Configuring Network Port Numbers
================================

This chapter lists port number assignments required to maintain communication between Ambari Server, Ambari Agents, and Ambari Web.

Default Network Port Numbers
____________________________

The following table lists the default ports used by Ambari Server and Ambari Agent services.

+---------------+--------------------+----------+--------------------------------------------------------------------+
| Service       | Servers            | Protocol | Description                                                        |
+===============+====================+==========+====================================================================+
| Ambari Server | Ambari Server host | http     | Interface to Ambari Web and Ambari REST API                        |
+---------------+--------------------+----------+--------------------------------------------------------------------+
| Ambari Server | Ambari Server host | https    | Handshake Port for Ambari Agents to Ambari Server                  |
+---------------+--------------------+----------+--------------------------------------------------------------------+
| Ambari Server | Ambari Server host | https    | Registration and Heartbeat Port for Ambari Agents to Ambari Server |
+---------------+--------------------+----------+--------------------------------------------------------------------+
| Ambari Agent  | All hosts          | tcp      | Ping port used for alerts to check the health of the Ambari Agent  |
+---------------+--------------------+----------+--------------------------------------------------------------------+

Optional: Changing the Default Ambari Server Port
_________________________________________________

By default, Ambari Server uses port 8080 to access the Ambari Web UI and the REST API.
To change the port number, you must edit the Ambari properties file.

Ambari Server should not be running when you change port numbers.
Edit ``ambari.properties`` before you start Ambari Server the first time or stop Ambari Server before editing properties.

1. On the Ambari Server host, open ``/etc/ambari-server/conf/ambari.properties`` with a text editor.

2. Add the client API port property and set it to your desired port value:

  ::

    client.api.port=<port_number>

3. Start or re-start the Ambari Server. Ambari Server now accesses Ambari Web via the newly configured port:

  ::

    http://<your.ambari.server>:<port_number>
