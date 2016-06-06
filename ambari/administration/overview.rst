Administering Ambari: Overview
==============================

Apache Ambari is a system to help you provision, manage and monitor |fdd| clusters.
This guide is intended for Cluster Operators and System Administrators responsible for installing and maintaining Ambari and the |fdd| clusters managed by Ambari.
Installing Ambari creates a default user with Ambari Admin privilege, with the following username/password: `admin/admin`.

When you sign into Ambari as Ambari Admin, you can:

* :doc:`Perform Ambari Admin Tasks</ambari/administration/admin-tasks>`
* :ref:`Create and Manage a Cluster<ambari-creating-cluster>`
* :doc:`Manage Users and Groups</ambari/administration/user-group>`
* :doc:`Manage Views</ambari/administration/views>`

Terms and Definitions
_____________________

The following basic terms help describe the key concepts associated with Ambari Administration.

+--------------+----------------------------------------------------------------+
| Term         | Definition                                                     |
+==============+================================================================+
| Ambari Admin | Specific privilege granted to a user that enables the user to  |
|              | administer Ambari. The default user admin created by Ambari is |
|              | flagged as an “Ambari Admin”. Users with the Ambari Admin      |
|              | privilege can grant, or revoke this privilege on other users.  |
+--------------+----------------------------------------------------------------+
| Account      | User name, password and privileges.                            |
+--------------+----------------------------------------------------------------+
| Cluster      | Installation of a |fdd| cluster, based on a particular Stack,  |
|              | that is managed by Ambari.                                     |
+--------------+----------------------------------------------------------------+
| Group        | Unique group of users in Ambari.                               |
+--------------+----------------------------------------------------------------+
| Group Type   | Local and LDAP. Local groups are maintained in the Ambari      |
|              | database. LDAP groups are imported (and synchronized) with an  |
|              | external LDAP (if configured).                                 |
+--------------+----------------------------------------------------------------+
| Permissions  | Represents the permission that can be granted to a principal   |
|              | (user or group) on a particular resource. For example, cluster |
|              | resources support Operator and Read-Only permissions.          |
+--------------+----------------------------------------------------------------+
| Principal    | User or group that can be authenticated by Ambari.             |
+--------------+----------------------------------------------------------------+
| Privilege    | Represents the mapping of a principal to a permission and a    |
|              | resource. For example: the user `admin` is granted the         |
|              | permission Operator on cluster DevCluster.                     |
+--------------+----------------------------------------------------------------+
| Resource     | Represents the resource available and managed in Ambari.       |
|              | Ambari supports two types of resources: cluster and view.      |
|              | An Ambari Admin assigns permissions for a resource for users   |
|              | and groups.                                                    |
+--------------+----------------------------------------------------------------+
| User         | Unique user in Ambari.                                         |
+--------------+----------------------------------------------------------------+
| User Type    | Local and LDAP. Local users are maintained in the Ambari       |
|              | database and authentication is performed against the Ambari    |
|              | database. LDAP users are imported (and synchronized) with an   |
|              | external LDAP (if configured).                                 |
+--------------+----------------------------------------------------------------+
| Version      | Represents a Stack version, which includes a set of            |
|              | repositories to install that version on a cluster. For more    |
|              | information about Stack versions.                              |
+--------------+----------------------------------------------------------------+
| View         | Defines a user interface component that is available to Ambari.|
+--------------+----------------------------------------------------------------+



Logging in to Ambari
____________________

After installing Ambari, you can log in to Ambari as follows:

1. Enter the following URL in a web browser:

  ::

    http://<your.ambari.server>:8080

  where ``<your.ambari.server>`` is the hostname for your Ambari server machine and ``8080`` is the default HTTP port.

2. Enter the user account credentials for the default administrative user automatically created during install:

  ::

    username/password = admin/admin

3. The :ref:`Ambari Administration web page<ambari-administration-interface>` displays. From this page you can :doc:`Manage Users and Groups</ambari/administration/user-group>`, :doc:`Manage Views</ambari/administration/views>`, Manage Stack and Versions, and :ref:`Create a Cluster<ambari-creating-cluster>`.

.. _ambari-administration-interface:

About the Ambari Administration Interface
_________________________________________

When you log in to the Ambari Administration interface with "Ambari Admin" privilege, a landing page displays links to the operations available. Plus, the operations are available from the left menu for clusters, views, users, and groups.

.. image:: /img/ambari/Ambari_Admin_page.png

* Clusters displays a link to a cluster (if created) and links to manage access permissions for that cluster. See :ref:`Creating a Cluster<ambari-creating-cluster>` for more information.
* User and Group Management provides the ability create and edit users and groups. See :doc:`Managing Users and Groups</ambari/administration/user-group>` for more information.
* Views lets you to create and edit instances of deployed Views and manage access permissions for those instances. See :doc:`Managing Views</ambari/administration/views>` for more information.
* Versions provides the ability to manage the Stack versions that are available for the clusters. See Managing Stack and Versions for more information.