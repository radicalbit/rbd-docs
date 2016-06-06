Managing Admin Credentials
==========================

When you enable Kerberos, if you choose to use an **Existing MIT KDC** or **Existing Active Directory**, the Kerberos Wizard prompts for information related to the KDC, the KDC Admin Account credentials and the Service and Ambari principals.
Once provided, Ambari will automatically create principals, generate keytabs and distribute keytabs to the hosts in the cluster.
The services will be configured for Kerberos and the service components are restarted to authenticate against the KDC.
This is the **Kerberos Automated Setup** option.

By default, Ambari will not retain the KDC Admin Account credentials you provide unless you have configured to :doc:`encrypt the passwords stored in Ambari</ambari/security/advanced-security/encrypt-database>`.
If you have not configured Ambari for password encryption, you will be prompted to provide KDC Admin Account credentials whenever cluster changes are made that require KDC principal and/or keytab changes (such as adding services, components and hosts).

If you have configured Ambari for password encryption, you will have an option to Save Admin Credentials.
Ambari will use the retained KDC Admin Account credentials to make the KDC changes automatically.

.. image:: /img/ambari/Save_Admin_Creds.png

.. Important::
  If you **do not** have password encryption enabled for Ambari, the Save Admin Credentials option **will not be** enabled.

**Updating KDC Credentials**

If you have chosen to Save Admin Credentials when enabling Kerberos, you can update or remove the credentials from Ambari using the following:

#. In Ambari Web, browse to **Admin > Kerberos** and click the **Manage KDC Credentials** button. The Manage KDC Credentials dialog is displayed.
#. If credentials have been previously saved, click **Remove** to remove the credentials currently stored in Ambari. Once removed, if cluster changes that require KDC principal and/or keytab changes (such as adding services, components and hosts), you will be prompted to enter the KDC Admin Account credentials.
#. Alternatively, to update the KDC Admin Account credentials, enter the Admin principal and password values and click **Save**.