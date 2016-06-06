Using Non-Default Databases
===========================

The following sections describe how to use Ambari with an existing database, other than the embedded PostgreSQL database instance that Ambari Server uses by default.

* :ref:`Using Ambari with Oracle<ambari-oracle-db>`
* :ref:`Using Ambari with MySQL<ambari-mysql-db>`
* :ref:`Using Ambari with PostgreSQL<ambari-postgresql-db>`
* :ref:`Troubleshooting Non-Default Databases with Ambari<ambari-db-troubleshooting>`

.. Note::
  For High Availability (HA) purposes, it is required that the relational database used with Ambari is also made highly available following best practices for the given database type.

.. _ambari-oracle-db:

Using Ambari with Oracle
________________________

To set up Oracle for use with Ambari:

1. On the Ambari Server host, install the appropriate ``JDBC.jar`` file.

  * Download the Oracle JDBC (OJDBC) driver from `here <http://www.oracle.com/technetwork/database/features/jdbc/index-091264.html>`_.
  * For **Oracle Database 11g**: select ``Oracle Database 11g Release 2 drivers > ojdbc6.jar``.
  * For **Oracle Database 12c**: select ``Oracle Database 12c Release 1 drivers > ojdbc7.jar``.
  * Copy the .jar file to the Java share directory. For example:

    ::

      cp ojdbc7.jar /usr/share/java

  * Make sure the .jar file has the appropriate permissions. For example:

    ::

      chmod 644 /usr/share/java/ojdbc7.jar

2. Create a user for Ambari and grant that user appropriate permissions.

  For example, using the Oracle database admin utility, run the following commands:

  ::

    # sqlplus sys/root as sysdba
    CREATE USER <AMBARIUSER> IDENTIFIED BY <AMBARIPASSWORD> default tablespace “USERS” temporary tablespace “TEMP”;
    GRANT unlimited tablespace to <AMBARIUSER>;
    GRANT create session to <AMBARIUSER>;
    GRANT create TABLE to <AMBARIUSER>;
    GRANT create SEQUENCE to <AMBARIUSER>;
    QUIT;

  Where ``<AMBARIUSER>`` is the Ambari user name and ``<AMBARIPASSWORD>`` is the Ambari user password.

3. Load the Ambari Server database schema.

  * You must pre-load the Ambari database schema into your Oracle database using the schema script.

    ::

      sqlplus <AMBARIUSER>/<AMBARIPASSWORD> < Ambari-DDL-Oracle-CREATE.sql

  * Find the Ambari-DDL-Oracle-CREATE.sql file in the ``/var/lib/ambari-server/resources/`` directory of the Ambari Server host after you have installed Ambari Server.

4. When setting up the Ambari Server, select ``Advanced Database Configuration > Option [2] Oracle`` and respond to the prompts using the username/password credentials you created in step 2.

.. _ambari-mysql-db:

Using Ambari with MySQL
_______________________

To set up MySQL for use with Ambari:

1. On the Ambari Server host, install the connector.

  * install the connector

    ::

      yum install mysql-connector-java

  * Confirm that .jar is in the Java share directory.

    ::

      ls /usr/share/java/mysql-connector-java.jar

  * Make sure the .jar file has the appropriate permissions - 644.

2. Create a user for Ambari and grant it permissions. For example, using the MySQL database admin utility:

  ::

    # mysql -u root -p
    CREATE USER '<AMBARIUSER>'@'%' IDENTIFIED BY '<AMBARIPASSWORD>';
    GRANT ALL PRIVILEGES ON *.* TO '<AMBARIUSER>'@'%';
    CREATE USER '<AMBARIUSER>'@'localhost' IDENTIFIED BY '<AMBARIPASSWORD>';
    GRANT ALL PRIVILEGES ON *.* TO '<AMBARIUSER>'@'localhost';
    CREATE USER '<AMBARIUSER>'@'<AMBARISERVERFQDN>' IDENTIFIED BY '<AMBARIPASSWORD>';
    GRANT ALL PRIVILEGES ON *.* TO '<AMBARIUSER>'@'<AMBARISERVERFQDN>';
    FLUSH PRIVILEGES;

  Where ``<AMBARIUSER>`` is the Ambari user name, ``<AMBARIPASSWORD>`` is the Ambari user password and ``<AMBARISERVERFQDN>`` is the Fully Qualified Domain Name of the Ambari Server host.

3. Load the Ambari Server database schema.

  ::

    mysql -u <AMBARIUSER> -p
    CREATE DATABASE <AMBARIDATABASE>;
    USE <AMBARIDATABASE>;
    SOURCE Ambari-DDL-MySQL-CREATE.sql;

  Where ``<AMBARIUSER>`` is the Ambari user name and ``<AMBARIDATABASE>`` is the Ambari database name.

  Find the ``Ambari-DDL-MySQL-CREATE.sql`` file in the ``/var/lib/ambari-server/resources/`` directory of the Ambari Server host after you have installed Ambari Server.

4. When setting up the Ambari Server, select ``Advanced Database Configuration > Option [3] MySQL`` and enter the credentials you defined in Step 2. for user name, password and database name.

.. _ambari-postgresql-db:

Using Ambari with PostgreSQL
____________________________

To set up PostgreSQL for use with Ambari:

1. Create a user for Ambari and grant it permissions.

  ::

    # sudo -u postgres psql
    CREATE DATABASE <AMBARIDATABASE>;
    CREATE USER <AMBARIUSER> WITH PASSWORD ‘<AMBARIPASSWORD>’;
    GRANT ALL PRIVILEGES ON DATABASE <AMBARIDATABASE> TO <AMBARIUSER>;
    \connect <AMBARIDATABASE>;
    CREATE SCHEMA <AMBARISCHEMA> AUTHORIZATION <AMBARIUSER>;
    ALTER SCHEMA <AMBARISCHEMA> OWNER TO <AMBARIUSER>;
    ALTER ROLE <AMBARIUSER> SET search_path to ‘<AMBARISCHEMA>’, 'public';

  Where ``<AMBARIUSER>`` is the Ambari user name ``<AMBARIPASSWORD>`` is the Ambari user password, ``<AMBARIDATABASE>`` is the Ambari database name and ``<AMBARISCHEMA>`` is the Ambari schema name.

2. Load the Ambari Server database schema.

  ::

    # psql -U <AMBARIUSER> -d <AMBARIDATABASE>
    \connect <AMBARIDATABASE>;
    \i Ambari-DDL-Postgres-CREATE.sql;

  Find the ``Ambari-DDL-Postgres-CREATE.sql`` file in the ``/var/lib/ambari-server/resources/`` directory of the Ambari Server host after you have installed Ambari Server.

3. When setting up the Ambari Server, select ``Advanced Database Configuration > Option[4] PostgreSQL`` and enter the credentials you defined in Step 2. for user name, password, and database name.

.. _ambari-db-troubleshooting:

Troubleshooting
_______________

Use these topics to help troubleshoot any issues you might have installing Ambari with an existing Oracle database.

**Problem: Ambari Server Fails to Start: No Driver**

Check ``/var/log/ambari-server/ambari-server.log`` for the following error:

::

  ExceptionDescription:Configurationerror.Class[oracle.jdbc.driver.OracleDriver] not found.

The Oracle JDBC.jar file cannot be found.

**Solution**: Make sure the file is in the appropriate directory on the Ambari server and re-run ambari-server setup. Review the load database procedure appropriate for your database type in :doc:`Using Non-Default Databases - Ambari<non-default-db>`.

**Problem: Ambari Server Fails to Start: No Connection**

Check ``/var/log/ambari-server/ambari-server.log`` for the following error:

::

  The Network Adapter could not establish the connection Error Code: 17002

Ambari Server cannot connect to the database.

**Solution**: Confirm that the database host is reachable from the Ambari Server and is correctly configured by reading ``/etc/ambari-server/conf/ambari.properties``.

::

  server.jdbc.url=jdbc:oracle:thin:@oracle.database.hostname:1521/ambaridb
  server.jdbc.rca.url=jdbc:oracle:thin:@oracle.database.hostname:1521/ambari

**Problem: Ambari Server Fails to Start: Bad Username**

Check ``/var/log/ambari-server/ambari-server.log`` for the following error:

::

  Internal Exception: java.sql.SQLException:ORA­01017: invalid username/password; logon denied

You are using an invalid username/password.

**Solution**: Confirm the user account is set up in the database and has the correct privileges.

**Problem: Ambari Server Fails to Start: No Schema**

Check ``/var/log/ambari-server/ambari-server.log`` for the following error:

::

  Internal Exception: java.sql.SQLSyntaxErrorException: ORA­00942: table or view does not exist

The schema has not been loaded.

**Solution**: Confirm you have loaded the database schema. Review the load database schema procedure appropriate for your database type in :doc:`Using Non-Default Databases - Ambari<non-default-db>`.