Disabling Kerberos Security
===========================

After :doc:`Enabling Kerberos Security<enable-security>`, you can disable Kerberos.

#. Log in to Ambari Web and Browse to Admin > Kerberos.
#. Click **Disable Kerberos** to launch the wizard.
#. Complete the wizard.

.. Note::
 If you have enabled Kerberos with an Automated Setup option, Ambari will attempt to contact the KDC and remove the principals created by Ambari.
 If the KDC is unavailable, the wizard will fail on the Unkerberize step.
 You can choose to ignore and continue the failure but removal of principals from the KDC will not be performed.