Optional: Set Up Two-Way SSL Between Ambari Server and Ambari Agents
====================================================================

Two-way SSL provides a way to encrypt communication between Ambari Server and Ambari Agents.
By default Ambari ships with Two-way SSL disabled. To enable Two-way SSL:

Ambari Server should not be running when you do this: either make the edits before you start Ambari Server the first time or bring the server down to make the edits.

1. On the Ambari Server host, open ``/etc/ambari-server/conf/ambari.properties`` with a text editor.

2. Add the following property:

  ::

    security.server.two_way_ssl = true

3. Start or restart the Ambari Server.

  ::

    ambari-server restart

The Agent certificates are downloaded automatically during Agent Registration.