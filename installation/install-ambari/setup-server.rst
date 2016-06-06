Set Up the Ambari Server
========================

Before starting the Ambari Server, you must set up the Ambari Server. Setup configures Ambari to talk to the Ambari database, installs the JDK and allows you to customize the user account the Ambari Server daemon will run as. The ambari-server setup command manages the setup process. Run the following command on the Ambari server host to start the setup process. You may also append :ref:`Setup Options<ambari-setup-options>` to the command.
::

  ambari-server setup

Respond to the setup prompt:

1. If you have not temporarily disabled SELinux, you may get a warning. Accept the default ``y``, and continue.

2. By default, Ambari Server runs under ``root``. Accept the default ``n`` at the ``Customize user account for ambari-server daemon`` prompt, to proceed as ``root``. If you want to create a different user to run the Ambari Server, or to assign a previously created user, select ``y`` at the ``Customize user account for ambari-server daemon`` prompt, then provide a user name. Refer to :doc:`Configuring Ambari for Non-Root</ambari/security/advanced-security/non-root-config>`, for more information about running the Ambari Server as non-root.

3. If you have not temporarily disabled ``iptables`` you may get a warning. Enter ``y`` to continue.

4. Select a JDK version to download. Enter 1 to download Oracle JDK 1.8.

  .. Note::
    JDK support depends entirely on your choice of |rbd-stack| Stack versions. Please refer to the :doc:`Ambari Reference Guide</ambari/reference/index-ambari-reference>` to see which JDK versions are supported by the |rbd-stack| Stack version you intend to install. By default, Ambari Server setup downloads and installs Oracle JDK 1.8 and the accompanying Java Cryptography Extension (JCE) Policy Files. If you plan to use a different version of the JDK, see :ref:`Setup Options<ambari-setup-options>` for more information.

5. Accept the Oracle JDK license when prompted. You must accept this license to download the necessary JDK from Oracle. The JDK is installed during the deploy phase.

6. Select ``n`` at ``Enter advanced database configuration`` to use the default, embedded PostgreSQL database for Ambari. The default PostgreSQL database name is ``ambari``. The default user name and password are ``ambari/bigdata``. Otherwise, to use an existing PostgreSQL, MySQL or Oracle database with Ambari, select ``y``. If you are using an existing PostgreSQL, MySQL, or Oracle database instance, use one of the following prompts:

  * To use an existing Oracle instance, and select your own database name, user name, and password for that database, enter ``2``. Select the database you want to use and provide any information requested at the prompts, including host name, port, Service Name or SID, user name, and password.

  * To use an existing MySQL database, and select your own database name, user name, and password for that database, enter ``3``. Select the database you want to use and provide any information requested at the prompts, including host name, port, database name, user name, and password.

  * To use an existing PostgreSQL database, and select your own database name, user name, and password for that database, enter ``4``. Select the database you want to use and provide any information requested at the prompts, including host name, port, database name, user name, and password.

  .. Important::
    You must prepare a non-default database instance, using the steps detailed in :doc:`Using Non-Default Databases-Ambari</ambari/reference/non-default-db>`, before running setup and entering advanced database configuration.

7. At Proceed with configuring remote database connection properties choose ``y``.

8. Setup completes.

  .. Note::
    If your host accesses the Internet through a proxy server, you must configure Ambari Server to use this proxy server. See :doc:`How to Set Up an Internet Proxy Server for Ambari</ambari/reference/internet-proxy>` for more information.

.. _ambari-setup-options:

Setup Options
_____________

The following table describes options frequently used for Ambari Server setup.

* **-j (or --java-home)**

  Specifies the JAVA_HOME path to use on the Ambari Server and all hosts in the cluster. By default when you do not specify this option, Ambari Server setup downloads the Oracle JDK 1.8 binary and accompanying Java Cryptography Extension (JCE) Policy Files to /var/lib/ambari-server/resources. Ambari Server then installs the JDK to /usr/jdk64.

  Use this option when you plan to use a JDK other than the default Oracle JDK 1.8. See JDK Requirements for more information on the supported JDKs. If you are using an alternate JDK, you must manually install the JDK on all hosts and specify the Java Home path during Ambari Server setup. If you plan to use Kerberos, you must also install the JCE on all hosts.

  This path must be valid on all hosts. For example:

  ::

    ambari-server setup –j /usr/java/default

* **--jdbc-driver**

  Should be the path to the JDBC driver JAR file. Use this option to specify the location of the JDBC driver JAR and to make that JAR available to Ambari Server for distribution to cluster hosts during configuration. Use this option with the --jdbc-db option to specify the database type.


* **--jdbc-db**

  Specifies the database type. Valid values are: [postgres|mysql|oracle] Use this option with the --jdbc-driver option to specify the location of the JDBC driver JAR file.


* **-s (or --silent)**

  Setup runs silently. Accepts all the default prompt values, such as:

  * User account "root" for the ambari-server
  * Oracle 1.8 JDK (which is installed at /usr/jdk64). This can be overridden by adding the -j option and specifying an existing JDK path.
  * Embedded PostgreSQL for Ambari DB (with database name "ambari")

  If you want to run the Ambari Server as non-root, you must run setup in interactive mode. When prompted to customize the ambari-server user account, provide the account information. Refer to :doc:`Configuring Ambari for Non-Root</ambari/security/advanced-security/non-root-config>` for more information.

* **-v (or --verbose)**

  Prints verbose info and warning messages to the console during Setup.

* **-g (or --debug)**

  Start Ambari Server in debug mode