Installing and Configuring the KDC
==================================

Ambari is able to configure Kerberos in the cluster to work with an existing MIT KDC, or existing Active Directory installation.
This section describes the steps necessary to prepare for this integration.

You can choose to have Ambari connect to the KDC and automatically create the necessary Service and Ambari principals, generate and distribute the keytabs (“Automated Kerberos Setup”). Ambari also provides an advanced option to manually configure Kerberos. If you choose this option, you must create the principals, generate and distribute the keytabs. Ambari will not do this automatically (“Manual Kerberos Setup”).

* :ref:`Use an Existing MIT KDC<ambari-use-existing-mit-kdc>`
* :ref:`Use an Existing Active Directory<ambari-use-existing-ad>`
* :ref:`Use Manual Kerberos Setup<ambari-use-manual-kerberos-setup>`

.. _ambari-use-existing-mit-kdc:

Use an Exisiting MIT KDC
________________________

To use an existing MIT KDC for the cluster, you must prepare the following:

* Ambari Server and cluster hosts have network access to both the KDC and KDC admin hosts.
* KDC administrative credentials are on-hand.

Proceed with :doc:`Enabling Kerberos Security in Ambari<enable-security>`.

.. Note::
  You will be prompted to enter the KDC Admin Account credentials during the Kerberos setup so that Ambari can contact the KDC and perform the necessary principal and keytab generation. By default, Ambari will not retain the KDC credentials unless you have configured Ambari for encrypted passwords.

.. _ambari-use-existing-ad:

Use an Existing Active Directory
________________________________

To use an existing Active Directory domain for the cluster with Automated Kerberos Setup, you must prepare the following:

* Ambari Server and cluster hosts have network access to, and be able to resolve the DNS names of, the Domain Controllers.
* Active Directory secure LDAP (LDAPS) connectivity has been configured.
* Active Directory User container for principals has been created and is on-hand. For example, ``OU=Radicalbit,OU=People,dc=apache,dc=org``
* Active Directory administrative credentials with delegated control of ``Create, delete, and manage user accounts`` on the previously mentioned User container are on-hand.

Proceed with :doc:`Enabling Kerberos Security in Ambari<enable-security>`.

.. Note::
  You will be prompted to enter the KDC Admin Account credentials during the Kerberos setup so that Ambari can contact the KDC and perform the necessary principal and keytab generation. By default, Ambari will not retain the KDC credentials unless you have configured Ambari for encrypted passwords.


.. _ambari-use-manual-kerberos-setup:

Use Manual Kerberos Setup
_________________________

To perform Manual Kerberos Setup, you must prepare the following:

* Cluster hosts have network access to the KDC.
* Kerberos client utilities (such as kinit) have been installed on every cluster host.
* The Java Cryptography Extensions (`JCE <http://docs.oracle.com/javase/7/docs/technotes/guides/security/crypto/CryptoSpec.html>`_) have been setup on the Ambari Server host and all hosts in the cluster.
* The Service and Ambari Principals will be manually created in the KDC before completing this wizard.
* The keytabs for the Service and Ambari Principals will be manually created and distributed to cluster hosts before completing this wizard.

Proceed with :doc:`Enabling Kerberos Security in Ambari<enable-security>`.
