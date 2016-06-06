Administering the Cluster
=========================

From the cluster dashboard, use the Admin options to view information about Service Accounts and to Enable Kerberos security.

.. Note::
  For more information about administering your Ambari Server, see the :doc:`Ambari Administration Guide</ambari/administration/index-ambari-administration>`.

Service Accounts
________________

To view the list of users and groups used by the cluster services, choose ``Admin > Service Accounts``.

.. image:: /img/ambari/service_accounts.png

Kerberos
________

If Kerberos has not been enabled in your cluster, click the Enable Kerberos button to launch the Kerberos wizard. For more information on configuring Kerberos in your cluster, see the :doc:`Ambari Security Guide</ambari/security/kerberos/index-ambari-kerberos>`. Once Kerberos is enabled, you can:

* Regenerate Keytabs
* Disable Kerberos

**How To Regenerate Keytabs**

#. Browse to ``Admin > Kerberos``.
#. Click the ``Regenerate Kerberos`` button.
#. Confirm your selection to proceed.
#. Optionally, you can regenerate keytabs for only those hosts that are missing keytabs. For example, hosts that were not online/available from Ambari when enabling Kerberos.
#. Once you confirm, Ambari will connect to the KDC and regenerate the keytabs for the Service and Ambari principals in the cluster.
#. Once complete, you must restart all services for the new keytabs to be used.

.. Note::
  Ambari requires the Kerberos Admin credentials in order to regenerate the keytabs. If the credentials are not available to Ambari, you will be prompted to enter the KDC Admin username and password. For more information on configuring Kerberos in your cluster, see the :doc:`Ambari Security Guide</ambari/security/kerberos/index-ambari-kerberos>`.

**How To Disable Kerberos**

#. Browse to ``Admin > Kerberos``.
#. Click the ``Disable Kerberos`` button.
#. Confirm your selection to proceed. Cluster services will be stopped and the Ambari Kerberos security settings will be reset.
#. To re-enable Kerberos, click Enable Kerberos and follow the wizard steps. For more information on configuring Kerberos in your cluster, see the :doc:`Ambari Security Guide</ambari/security/kerberos/index-ambari-kerberos>`.