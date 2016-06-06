Configuring Ambari for LDAP or Active Directory Authentication
==============================================================

By default Ambari uses an internal database as the user store for authentication and authorization.
If you want to configure LDAP or Active Directory (AD) external authentication, you need to :ref:`collect the following information<ambari-setup-ldap-auth>` and :ref:`run a setup command<ambari-use-ldap-server>`.

Also, you must :ref:`synchronize your LDAP users and groups<ambari-synchronize-ldap>` into the Ambari DB to be able to manage authorization and permissions against those users and groups.

.. Note:
  When synchronizing LDAP users and groups, Ambari uses LDAP results paging controls to synchronize large numbers of LDAP objects.
  Most modern LDAP servers support these control, but for those that do not, such as Oracle Directory Server Enterprise Edition 11g, Ambari introduces a configuration parameter to disable pagination.
  The ``authentication.ldap.pagination.enabled`` property can be set to false in the ``/etc/ambari-server/conf/ambari-properties`` file to disable result paging controls.
  This will limit the maximum number of entities that can be imported at any given time to the maximum result limit of the LDAP server.
  To work around this, import sets of users or groups using the -users and -groups options covered in section :ref:`Specific Set of Users and Groups<ambari-specific-set-of-users-groups>`.

.. _ambari-setup-ldap-auth:

Setting Up LDAP User Authentication
___________________________________

The following table details the properties and values you need to know to set up LDAP authentication.

.. Note::
  If you are going to set ``bindAnonymously`` to false (the default), you need to make sure you have an LDAP Manager name and password set up. If you are going to use SSL, you need to make sure you have already set up your certificate and keys.

Ambari Server LDAP Properties:

+-----------------------------------------+---------------------------+------------------------------------------------------------------------------------------------------------------------------------------+
| Property                                | Values                    | Description                                                                                                                              |
+=========================================+===========================+==========================================================================================================================================+
| authentication.ldap.primaryUrl          | server:port               | The hostname and port for the LDAP or AD server. Example: my.ldap.server:389                                                             |
+-----------------------------------------+---------------------------+------------------------------------------------------------------------------------------------------------------------------------------+
| authentication.ldap.secondaryUrl        | server:port               | The hostname and port for the secondary LDAP or AD server. Example: my.secondary.ldap.server:389 This is an optional value.              |
+-----------------------------------------+---------------------------+------------------------------------------------------------------------------------------------------------------------------------------+
| authentication.ldap.useSSL              | true or false             | If true, use SSL when connecting to the LDAP or AD server.                                                                               |
+-----------------------------------------+---------------------------+------------------------------------------------------------------------------------------------------------------------------------------+
| authentication.ldap.usernameAttribute   | [LDAP attribute]          | The attribute for username. Example: uid                                                                                                 |
+-----------------------------------------+---------------------------+------------------------------------------------------------------------------------------------------------------------------------------+
| authentication.ldap.baseDn              | [Distinguished Name]      | The root Distinguished Name to search in the directory for users. Example: ou=people,dc=hadoop,dc=apache,dc=org                          |
+-----------------------------------------+---------------------------+------------------------------------------------------------------------------------------------------------------------------------------+
| authentication.ldap.referral            | [Referral method]         | Determines if LDAP referrals should be followed, or ignored.                                                                             |
+-----------------------------------------+---------------------------+------------------------------------------------------------------------------------------------------------------------------------------+
| authentication.ldap.bindAnonymously     | true or false             | If true, bind to the LDAP or AD server anonymously                                                                                       |
+-----------------------------------------+---------------------------+------------------------------------------------------------------------------------------------------------------------------------------+
| authentication.ldap.managerDn           | [Full Distinguished Name] | If Bind anonymous is set to false, the Distinguished Name (“DN”) for the manager. Example: uid=hdfs,ou=people,dc=hadoop,dc=apache,dc=org |
+-----------------------------------------+---------------------------+------------------------------------------------------------------------------------------------------------------------------------------+
| authentication.ldap.managerPassword     | [password]                | If Bind anonymous is set to false, the password for the manager                                                                          |
+-----------------------------------------+---------------------------+------------------------------------------------------------------------------------------------------------------------------------------+
| authentication.ldap.userObjectClass     | [LDAP Object Class]       | The object class that is used for users. Example: organizationalPerson                                                                   |
+-----------------------------------------+---------------------------+------------------------------------------------------------------------------------------------------------------------------------------+
| authentication.ldap.groupObjectClass    | [LDAP Object Class]       | The object class that is used for groups. Example: groupOfUniqueNames                                                                    |
+-----------------------------------------+---------------------------+------------------------------------------------------------------------------------------------------------------------------------------+
| authentication.ldap.groupMembershipAttr | [LDAP attribute]          | The attribute for group membership. Example: uniqueMember                                                                                |
+-----------------------------------------+---------------------------+------------------------------------------------------------------------------------------------------------------------------------------+
| authentication.ldap.groupNamingAttr     | [LDAP attribute]          | The attribute for group name.                                                                                                            |
+-----------------------------------------+---------------------------+------------------------------------------------------------------------------------------------------------------------------------------+

.. _ambari-use-ldap-server:

Configure Ambari to use LDAP Server
___________________________________

.. Note::
  **Only if you are using LDAPS**, and the LDAPS server certificate is signed by a trusted Certificate Authority, there is no need to import the certificate into Ambari so this section does not apply to you. If the LDAPS server certificate is self-signed, or is signed by an unrecognized certificate authority such as an internal certificate authority, you must import the certificate and create a keystore file. The following example creates a keystore file at ``/keys/ldaps-keystore.jks``, but you can create it anywhere in the file system:
  Run the LDAP setup command on the Ambari server and answer the prompts, using the information you collected above:

#. ``mkdir /etc/ambari-server/keys`` where the keys directory does not exist, but should be created.
#. ``$JAVA_HOME/bin/keytool -import -trustcacerts -alias root -file $PATH_TO_YOUR_LDAPS_CERT -keystore /etc/ambari-server/keys/ldaps-keystore.jks``
#. Set a password when prompted. You will use this during ``ambari-server setup-ldap``.

Then run:

::

  ambari-server setup-ldap

1. At the ``Primary URL*`` prompt, enter the server URL and port you collected above. Prompts marked with an asterisk are required values.

2. At the ``Secondary URL*`` prompt, enter the secondary server URL and port. This value is optional.

3. At the ``Use SSL*`` prompt, enter your selection. If using **LDAPS**, enter ``true``.

4. At the ``User object class*`` prompt, enter the object class that is used for users.

5. At the ``User name attribute*`` prompt, enter your selection. The default value is ``uid``.

6. At the ``Group object class*`` prompt, enter the object class that is used for groups.

7. At the ``Group name attribute*`` prompt, enter the attribute for group name.

8. At the ``Group member attribute*`` prompt, enter the attribute for group membership.

9. At the ``Distinguished name attribute*`` prompt, enter the attribute that is used for the distinguished name.

10. At the ``Base DN*`` prompt, enter your selection.

11. At the ``Referral method*`` prompt, enter to ``follow`` or ``ignore LDAP`` referrals.

12. At the ``Bind anonymously*`` prompt, enter your selection.

13. At the ``Manager DN*`` prompt, enter your selection if you have set **bind.Anonymously** to false

14. At the ``Enter the Manager Password*`` prompt, enter the password for your LDAP manager DN.

15. If you set ``Use SSL*`` = true in step 3, the following prompt appears: ``Do you want to provide custom TrustStore for Ambari?`` Consider the following options and respond as appropriate:

  * **More secure option**: If using a self-signed certificate that you do not want imported to the existing JDK keystore, enter ``y``. For example, you want this certificate used only by Ambari, not by any other applications run by JDK on the same host. If you choose this option, additional prompts appear. Respond to the additional prompts as follows:

    * At the ``TrustStore type`` prompt, enter ``jks``.
    * At the ``Path to TrustStore file`` prompt, enter ``/keys/ldaps-keystore.jks`` (or the actual path to your keystore file).
    * At the ``Password for TrustStore`` prompt, enter the password that you defined for the keystore.

  * **Less secure option**: If using a self-signed certificate that you want to import and store in the existing, default JDK keystore, enter ``n``.

    * Convert the SSL certificate to X.509 format, if necessary, by executing the following command (Where ``<slapd.crt>`` is the path to the X.509 certificate.):

      ::

        openssl x509 -in slapd.pem -out <slapd.crt>

    * Import the SSL certificate to the existing keystore, for example the default JRE certificates storage, using the following instruction (Where Ambari is set up to use JDK 1.7. Therefore, the certificate must be imported in the JDK 7 keystore.):

      ::

        /usr/jdk64/jdk1.7.0_45/bin/keytool -import -trustcacerts -file slapd.crt -keystore /usr/jdk64/jdk1.7.0_45/jre/lib/security/cacerts

16. Review your settings and if they are correct, select ``y``.

17. Start or restart the Server

  ::

    ambari-server restart

  The users you have just imported are initially granted the Ambari User privilege.
  Ambari Users can read metrics, view service status and configuration, and browse job information.
  For these new users to be able to start or stop services, modify configurations, and run smoke tests, they need to be Admins.
  To make this change, as an Ambari Admin, use ``Manage Ambari > Users > Edit``.

.. _ambari-synchronize-ldap:

Synchronizing LDAP Users and Groups
___________________________________

Run the LDAP synchronize command and answer the prompts to initiate the sync:

::

  ambari-server sync-ldap [option]

.. Note::
  To perform this operation, your Ambari Server must be running.

  * When prompted, you must provide credentials for an Ambari Admin.
  * When syncing LDAP, Local user accounts with matching username will switch to LDAP type, which means their authentication will be against the external LDAP and not against the Local Ambari user store.
  * LDAP sync only syncs up-to-1000 users. If your LDAP contains over 1000 users and you plan to import over 1000 users, you must use the --users option when syncing and specify a filtered list of users to perform import in batches.

The utility provides three options for synchronization:

* Specific set of users and groups, or
* Synchronize the existing users and groups in Ambari with LDAP, or
* All users and groups

Review log files for failed synchronization attempts, at ``/var/log/ambari-server/ambari-server.log`` on the Ambari Server host.

.. Note:
  When synchronizing LDAP users and groups, Ambari uses LDAP results paging controls to synchronize large numbers of LDAP objects.
  Most modern LDAP servers support these control, but for those that do not, such as Oracle Directory Server Enterprise Edition 11g, Ambari introduces a configuration parameter to disable pagination.
  The ``authentication.ldap.pagination.enabled`` property can be set to false in the ``/etc/ambari-server/conf/ambari-properties`` file to disable result paging controls.
  This will limit the maximum number of entities that can be imported at any given time to the maximum result limit of the LDAP server.
  To work around this, import sets of users or groups using the -users and -groups options covered in section :ref:`Specific Set of Users and Groups<ambari-specific-set-of-users-groups>`.

.. _ambari-specific-set-of-users-groups:

Specific Set of Users and Groups
________________________________

::

  ambari-server sync-ldap --users users.txt --groups groups.txt

Use this option to synchronize a specific set of users and groups from LDAP into Ambari.
Provide the command a text file of comma-separated users and groups.
The comma separated entries in each of these files should be based off of the values in LDAP of the attributes chosen during setup.
The "User name attribute" should be used for the users.txt file, and the "Group name attribute" should be used for the ``groups.txt`` file.
This command will find, import, and synchronize the matching LDAP entities with Ambari.

.. Note::
  Group membership is determined using the Group Membership Attribute (``groupMembershipAttr``) specified during ``setup-ldap``.
  User name is determined by using the Username Attribute (``usernameAttribute``) specified during ``setup-ldap``.

Existing Users and Groups
_________________________

::

  ambari-server sync-ldap --existing

After you have performed a synchronization of a :ref:`specific set of users and groups<ambari-specific-set-of-users-groups>`, you use this option to synchronize only those entities that are in Ambari with LDAP.
Users will be removed from Ambari if they no longer exist in LDAP, and group membership in Ambari will be updated to match LDAP.

.. Note::
  Group membership is determined using the Group Membership Attribute specified during ``setup-ldap``.

All Users and Groups
____________________

.. Important::
  Only use this option if you are sure you want to synchronize all users and groups from LDAP into Ambari.
  If you only want to synchronize a subset of users and groups, use a specific set of users and groups option.

  ::

    ambari-server sync-ldap --all

  This will import all entities with matching LDAP user and group object classes into Ambari.