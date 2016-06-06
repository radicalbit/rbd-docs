Moving the Ambari Server
========================

To transfer an Ambari Server that uses the default, embedded, PostgreSQL database from one host to a new host, use the following instructions:

#. :ref:`Back up current data<ambari-backup-data>` - from the original Ambari Server database.
#. :ref:`Update all Agents<ambari-update-agents>` - to point to the new Ambari Server.
#. :ref:`Install the New Ambari Server<ambari-install-new-server>` - on the new host and populate databases with information from the original Server.

.. Note::
  If your Ambari Server is using one of the non-default databases (such as MySQL, Oracle, or an existing PostgreSQL instance) then be sure to follow backup, restore, and stop/start procedures that match that database type.

.. _ambari-backup-data:

Back up Current Data
____________________

1. On the Ambari Server host, stop the original Ambari Server.

  ::

    ambari-server stop

2. Create a directory to hold the database backups.

  ::

    cd /tmp
    mkdir dbdumps/
    cd dbdumps/

3. Create the database backups.

  ::

    pg_dump -U {ambari.db.username} -f ambari.sql
    Password: {ambari.db.password}

  where the following:

  +--------------------+------------------------+---------+
  | Variable           | Description            | Default |
  +====================+========================+=========+
  | ambari.db.username | The database username. | ambari  |
  +--------------------+------------------------+---------+
  | ambari.db.password | The database password. | bigdata |
  +--------------------+------------------------+---------+

4. Create a backup of the Ambari Server meta info.

  ::

    ambari-server backup

.. _ambari-update-agents:

Update all Agents
_________________

1. On each agent host, stop the agent

  ::

    ambari-agent stop

2. Remove old agent certificates (if any exist).

  ::

    rm /var/lib/ambari-agent/keys/*

3. Using a text editor, edit ``/etc/ambari-agent/conf/ambari-agent.ini`` to point to the new host.

  ::

    [server]
    hostname={new.ambari.server.fqdn}
    url_port=8440
    secured_url_port=8441

.. _ambari-install-new-server:

Install the New Ambari Server
_____________________________

1. Install the new Ambari Server on the new host.

  ::

    yum install ambari-server

2. Run setup the Ambari Server and setup similar to how the original Ambari Server is configured.

  ::

    ambari-server setup

3. Restart the PostgreSQL instance.

  ::

    service postgresql restart

4. Open the PostgreSQL interactive terminal.

  ::

    su - postgres
    psql

5. Using the interactive terminal, drop the ``ambari`` database created by the new ambari setup and install.

  ::

    drop database ambari;

6. Check to make sure the databases have been dropped. The "ambari" databases should not be listed.

  ::

    \l

7. Create new "ambari" database to hold the transferred data.

  ::

    create database ambari;

8. Exit the PostgreSQL interactive terminal.

  ::

    \q

9. Copy the saved data (``/tmp/dbdumps/ambari.sql``) from :ref:`Back up Current Data<ambari-backup-data>` to the new Ambari Server host.

10. Load the saved data into the new database.

  ::

    psql -d ambari -f /tmp/dbdumps/ambari.sql

11. Start the new Server.

  ::

    ambari-server start

12. On each Agent host, start the Ambari Agent.

  ::

    ambari-agent start

13. Open Ambari Web. Point your browser to:

  ::

    http://<new.Ambari.Server>:8080

The new Ambari Server is ready to use.