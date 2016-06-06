Ambari Admin Tasks
==================

An "Ambari Admin" has administrator (or super-user) privilege. When logged into Ambari with the "Ambari Admin" privilege, you can:

* :ref:`Change the Administrator Account Password<ambari-change-admin-password>`
* :ref:`Create a cluster<ambari-creating-cluster>`
* :ref:`Setting Cluster Permissions<ambari-cluster-permission>`
* :doc:`Managing Views</ambari/administration/views>`
* :ref:`Manage permissions for view instances<ambari-setting-view-permissions>`
* :doc:`Managing Users and Groups</ambari/administration/user-group>`

For more information about creating Ambari users locally and importing Ambari LDAP users, see :doc:`Managing Users and Groups</ambari/administration/user-group>`.


.. _ambari-change-admin-password:

Changing the Administrator Account Password
___________________________________________

During install and setup, the Cluster Installer wizard automatically creates a default user with "Ambari Admin" privilege. You can change the password for this user (or other Local users in the system) from the Ambari Administration interface. You can change the password for the default admin user to create a unique administrator credential for your system.

To change the password for the default admin account:

#. Browse to the Users section.
#. Select the admin user.
#. Click the Change Password button.
#. Enter the current admin password and the new password twice.
#. Click OK to save the new password.

.. _ambari-creating-cluster:

Creating a Cluster
__________________

As an Ambari Admin, you can launch the Cluster Install Wizard and create a cluster. To create a cluster, from the Ambari Administration interface:

#. Click ``Install Cluster``. The Cluster Install Wizard displays.
#. Follow the steps in the wizard to install your cluster.

For more information about prerequisites and system requirements, see :doc:`Getting Ready</installation/getting-ready/index-getting-ready>`.

.. _ambari-cluster-permission:

Setting Cluster Permissions
___________________________

After you create a cluster, users with Ambari Admin privileges automatically get Operator permission on the cluster. By default, no users have access to the cluster. You can grant permissions on the cluster to other users and groups from the Ambari Administration interface.

Ambari manages the following permissions for a cluster: ``Operator`` and ``Read-Only``. Users and Groups with ``Operator`` permission are granted access to the cluster. Operator permission provides full control of the following services:

* Start
* Stop
* Restart
* Add New

And the following configurations:

* Modify
* Revert

Users and Groups with ``Read-Only`` permission can only view, not modify, services and configurations.

Users with Ambari Admin privileges are implicitly granted ``Operator`` permission. Plus, Ambari Admin users have access to the Ambari Administration interface which allows them to control permissions for the cluster.

To modify user and group permissions for a cluster:

#. As an Ambari Admin, access the Ambari Administration interface.
#. Click Permissions, displayed under the cluster name.
#. The form showing the permissions ``Operator`` and ``Read-Only`` with users and groups is displayed.
#. Modify the users and groups mapped to each permission and save.

For more information about managing users and groups, see :doc:`Managing Users and Groups</ambari/administration/user-group>`.

.. Warning::
  Assigning permissions to a group having no members is possible.

.. Note::
  Verify user permissions, group membership, and group permissions to ensure that each user and group has appropriate permissions.

Viewing the Cluster Dashboard
_____________________________

After you have created a cluster, select ``Clusters`` > ``Go to Dashboard`` to open the Dashboard view. For more information about using Ambari to monitor and manage your cluster, see :doc:`Monitoring and Managing your RBD Cluster with Ambari</ambari/user-guide/monitor-manage-cluster>`.

Renaming a Cluster
__________________

A user with Ambari Admin privileges can rename a cluster, using the Ambari Administration interface.

To rename a cluster:

1. In Clusters, click the Rename Cluster icon, next to the cluster name.

  .. image:: /img/ambari/Rename_cluster.png

  The cluster name becomes writeable.

2. Enter alphanumeric characters as a cluster name.

3. Click the check mark.

4. Confirm

.. Important::
  After renaming the cluster, alert checks must be re-queued on the agents. Therefore, you must restart Ambari Server and the Ambari Agents for the change to take effect.

.. Important::
  By changing the name of the cluster, the Ambari REST API resource for the cluster also changes. You must adjust any API calls you make to use this new name.