Managing Users and Groups
=========================

An Ambari Admin can create and manage users and groups available to Ambari. An Ambari Admin can also import user and group information into Ambari from external LDAP systems. This section describes the specific tasks you perform when managing users and groups in Ambari.

* :ref:`Users and Groups Overview<ambari-user-group-overiview>`
* :ref:`Creating a Local User<ambari-create-local-user>`
* :ref:`Setting User Status<ambari-setting-user-status>`
* :ref:`Setting the Ambari Admin Flag<ambari-admin-flag>`
* :ref:`Changing the Password for a Local User<ambari-change-local-user-password>`
* :ref:`Deleting a Local User<ambari-delete-user>`
* :ref:`Creating a Local Group<ambari-create-group>`
* :ref:`Managing Group Membership<ambari-group-membership>`
* :ref:`Deleting a Local Group<ambari-delete-group>`

.. _ambari-user-group-overiview:

Users and Groups Overview
_________________________

Ambari supports two types of users and groups: Local and LDAP. The following topics describe how Ambari Administration supports managing Local and LDAP users and groups.

**Local and LDAP User and Group Types**

Local users are stored in and authenticate against the Ambari database. LDAP users have basic account information stored in the Ambari database. Unlike Local users, LDAP users authenticate against an external LDAP system.

Local groups are stored in the Ambari database. LDAP groups have basic information stored in the Ambari database, including group membership information. Unlike Local groups, LDAP groups are imported and synchronized from an external LDAP system.

To use LDAP users and groups with Ambari, you must configure Ambari to authenticate against an external LDAP system. For more information about running ambari-server setup-ldap, see :ref:`Configure Ambari to use LDAP Server<ambari-use-ldap-server>`. A new Ambari user or group, created either locally or by synchronizing against LDAP, is granted no privileges by default. You, as an Ambari Admin, must explicitly grant each user permissions to access clusters or views.

**Ambari Admin Privileges**

As an Ambari Admin, you can create new users, delete users, change user passwords and edit user settings. You can control certain privileges for Local and LDAP users. The following table lists the privileges available and those not available to the Ambari Admin for Local and LDAP Ambari users.

+------------------------------+---------------+---------------+
| Administrator User Privilege | Local User    | LDAP User     |
+==============================+===============+===============+
| Change Password              | Available     | Not Available |
+------------------------------+---------------+---------------+
| Set Ambari Admin Flag        | Available     | Available     |
+------------------------------+---------------+---------------+
| Change Group Membership      | Available     | Not Available |
+------------------------------+---------------+---------------+
| Delete User                  | Available     | Not Available |
+------------------------------+---------------+---------------+
| Set Active / Inactive        | Available     | Available     |
+------------------------------+---------------+---------------+

.. _ambari-create-local-user:

Creating a Local User
_____________________

To create a local user:

1. Browse to Users.

2. Click Create Local User.

3. Enter a unique user name.

  .. Note::
    All user names are converted to lowercase.

4. Enter a password, then confirm that password.

5. Click Save.

.. _ambari-setting-user-status:

Setting User Status
___________________

User status indicates whether the user is active and should be allowed to log into Ambari or should be inactive and denied the ability to log in. By setting the Status flag as Active or Inactive, you can effectively "disable" user account access to Ambari while preserving the user account information related to permissions.

To set user Status:

#. On the Ambari Administration interface, browse to Users.
#. Click the user name of the user to modify.
#. Click the Status control to toggle between Active or Inactive.
#. Choose OK to confirm the change. The change is saved immediately.

.. _ambari-admin-flag:

Setting the Ambari Admin Flag
_____________________________

You can elevate one or more users to have Ambari administrative privileges, by setting the Ambari Admin flag. You must be logged in as an account that is an Ambari Admin to set or remove the Ambari Admin flag.

To set the Ambari Admin Flag:

#. Browse to the Users section.
#. Click the user name you wish to modify.
#. Click on the Ambari Admin control.
#. Switch Yes to set, or No to remove the Admin flag.

.. Important::
  To prevent you from accidently locking yourself out of the Ambari Administration user interface, Ambari prevents setting the Ambari Admin flag for your own Ambari Admin account to No.

.. _ambari-change-local-user-password:

Changing the Password for a Local User
______________________________________

An Ambari Administrator can change local user passwords. LDAP passwords are not managed by Ambari since LDAP users authenticate to external LDAP. Therefore, LDAP user passwords cannot be changed from Ambari.

To change the password for a local user:

#. Browse to the user.
#. Click Change password.
#. Enter YOUR administrator password to confirm that you have privileges required to change a local user password.
#. Enter a password, then confirm that password.
#. Click Save.

.. _ambari-delete-user:

Deleting a Local User
_____________________

Deleting a local user removes the user account from the system, including all privileges associated with the user. You can reuse the name of a local user that has been deleted. To delete a local user:

#. Browse to the User.
#. Click Delete User.
#. Confirm.

.. Note::
  If you want to disable user log in, :ref:`set the user Status<ambari-setting-user-status>` to Inactive.

.. _ambari-create-group:

Creating a Local Group
______________________

To create a local group:

#. Browse to Groups.
#. Click Create Local Group.
#. Enter a unique group name.
#. Click Save

.. _ambari-group-membership:

Managing Group Membership
_________________________

You can manage group membership of Local groups by adding or removing users from groups.

**Adding a User to a Group**

To add a user to group:

#. Browse to Groups.
#. Click a name in the Group Name list.
#. Choose the Local Members control to edit the member list.
#. In the empty space, type the first character in an existing user name.
#. From the list of available user names, choose a user name.
#. Click the check mark to save the current, displayed members as group members.

**Modifying Group Membership**

To modify Local group membership:

#. In the Ambari Administration interface, browse to Groups.
#. Click the name of the Group to modify.
#. Choose the Local Members control to edit the member list.
#. Click in the Local Members text area to modify the current membership.
#. Click the X to remove a user.
#. To save your changes, click the checkmark. To discard your changes, click the ``x``.

.. _ambari-delete-group:

Deleting a Local Group
______________________

Deleting a local group removes all privileges associated with the group. To delete a local group:

#. Browse to the Group.
#. Click Delete Group.
#. Confirm. The group is deleted and the associated group membership information is removed.