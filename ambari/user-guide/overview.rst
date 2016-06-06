Overview: Ambari User's Guide
=============================

Hadoop is a large-scale, distributed data storage and processing infrastructure using clusters of commodity hosts networked together. Monitoring and managing such complex distributed systems is a non-trivial task. To help you manage the complexity, Apache Ambari collects a wide range of information from the cluster's nodes and services and presents it to you in an easy-to-read and use, centralized web interface, Ambari Web.

Ambari Web displays information such as service-specific summaries, graphs, and alerts. You use Ambari Web to create and manage your |rbd-stack| cluster and to perform basic operational tasks such as starting and stopping services, adding hosts to your cluster, and updating service configurations. You also can use Ambari Web to perform administrative tasks for your cluster such as enabling Kerberos security and performing Stack upgrades.

For more information on administering Ambari users, groups and views, refer to the :doc:`Ambari Administration Guide</ambari/administration/index-ambari-administration>`.


Architecture
____________

The Ambari Server serves as the collection point for data from across your cluster. Each host has a copy of the Ambari Agent - either installed automatically by the Install wizard or manually - which allows the Ambari Server to control each host.

Below an image of the architecture:

.. image:: /img/ambari/Ambari_architecture.png
  :align: center

**Sessions**

Ambari Web is a client-side JavaScript application, which calls the Ambari REST API (accessible from the Ambari Server) to access cluster information and perform cluster operations. After authenticating to Ambari Web, the application authenticates to the Ambari Server. Communication between the browser and server occurs asynchronously via the REST API.

The Ambari Web UI periodically accesses the Ambari REST API, which resets the session timeout. Therefore, by default, Ambari Web sessions do not timeout automatically. You can configure Ambari to timeout after a period of inactivity. Refer to :doc:`Ambari Web Inactivity Timeout</ambari/security/advanced-security/web-inactivity-timeout>` in the Ambari Security Guide for more information.

Accessing Ambari Web
____________________

Typically, you start the Ambari Server and Ambari Web as part of the installation process. If Ambari Server is stopped, you can start it using a command line editor on the Ambari Server host machine. Enter the following command:

::

  ambari-server start

To access Ambari Web, open a supported browser and enter the Ambari Web URL:

::

  http://<your.ambari.server>:8080

Enter your user name and password. If this is the first time Ambari Web is accessed, use the default values, ``admin/admin``.

These values can be changed, and new users provisioned, using the ``Manage Ambari`` option.