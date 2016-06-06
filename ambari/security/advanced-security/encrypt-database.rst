Optional: Encrypt Database and LDAP Passwords
=============================================

If you plan to configure Ambari to retain the Kerberos KDC Admin Account credentials when :doc:`Configuring Kerberos<ambari-server-kerberos>`, or you wish to encrypt the Ambari database and LDAP server passwords, you need to setup encryption for the passwords stored in the Ambari database.

Ambari Server should not be running when you do this: either make the edits before you start Ambari Server the first time or bring the server down to make the edits.
On the Ambari Server, run the special setup command and answer the prompts:

::

  ambari-server setup-security

* When prompted, select Option 2 to "Encrypt the passwords stored in ambari.properties file".
* Provide a master key for encrypting the passwords. You are prompted to enter the key twice for accuracy.
* Once the passwords are encrypted, you need access to the master key to start Ambari Server. You have three options for maintaining the master key:

  * Persist it to a file on the server by pressing y at the prompt.
  * Create an environment variable ``AMBARI_SECURITY_MASTER_KEY`` and set it to the key.
  * Provide the key manually at the prompt on server start up.

* Start the Ambari Server:

  ::

    ambari-server start

Reset Encryption
________________

There may be situations in which you want to:

* Remove encryption entirely
* Change the current master key, either because the key has been forgotten or because you want to change the current key as a part of a security routine. Ambari Server should not be running when you do this.

.. _ambari-remove-encryption-entirely:

Remove Encryption Entirely
__________________________

To reset Ambari database and LDAP passwords to a completely unencrypted state:

1. On the Ambari host, open ``/etc/ambari-server/conf/ambari.properties`` with a text editor and set this property

  ::

    security.passwords.encryption.enabled=false

2. Delete ``/var/lib/ambari-server/keys/credentials.jceks``

3. Delete ``/var/lib/ambari-server/keys/master``

4. You must now reset the database password and, if necessary, the LDAP password. Run ``ambari-server setup`` and ``ambari-server setup-ldap`` again.

Change the Current Master Key
_____________________________

To change the master key:

* If you know the current master key or if the current master key has been persisted:

  * Re-run the encryption setup command and follow the prompts.

    ::

      ambari-server setup-security

  * Select Option 2: Choose one of the following options:

    * [1] Enable HTTPS for Ambari server.
    * [2] Encrypt passwords stored in ambari.properties file.
    * [3] Setup Ambari kerberos JAAS configuration.

  * Enter the current master key when prompted if necessary (if it is not persisted or set as an environment variable).

  * At the ``Do you want to reset Master Key`` prompt, enter ``yes``.

  * At the prompt, enter the new master key and confirm.

* If you do not know the current master key:

  * Remove encryption entirely, as described :ref:`here<ambari-remove-encryption-entirely>`.
  * Re-run ``ambari-server setup-security`` as described at point one.
  * Start or restart the Ambari Server.

    ::

      ambari-server restart