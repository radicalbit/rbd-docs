Enabling Kerberos Security
==========================

Whether you choose automated or manual Kerberos setup, Ambari provides a wizard to help with enabling Kerberos in the cluster.
This section provides information on preparing Ambari before running the wizard, and the steps to run the wizard.

.. Important::
  Prerequisites for enabling Kererbos are having the `JCE <http://docs.oracle.com/javase/7/docs/technotes/guides/security/crypto/CryptoSpec.html>`_ installed on all hosts on the cluster (including the Ambari Server) and having the Ambari Server host as part of the cluster.
  This means the Ambari Server host should be running an Ambari Agent.

.. _ambari-install-jce:

Installing the JCE
__________________

Before enabling Kerberos in the cluster, you must deploy the Java Cryptography Extension (JCE) security policy files on the Ambari Server and on all hosts in the cluster.

.. Important::
  If you are using Oracle JDK, **you must** distribute and install the `JCE <http://docs.oracle.com/javase/7/docs/technotes/guides/security/crypto/CryptoSpec.html>`_ **on all hosts** in the cluster, including the Ambari Server.
  **Be sure to restart Ambari Server after installng the JCE**.
  If you are using OpenJDK, some distributions of the OpenJDK come with unlimited strength JCE automatically and therefore, installation of JCE is not required.

To install JCE:

1. On the Ambari Server, obtain the `JCE policy file <http://www.oracle.com/technetwork/java/javase/downloads/jce-7-download-432124.html>`_.

2. Save the policy file archive in a temporary location.

3. On Ambari Server and on each host in the cluster, add the unlimited security policy JCE jars to ``$JAVA_HOME/jre/lib/security/``.

  For example, run the following to extract the policy jars into the JDK installed on your host:

  ::

    unzip -o -j -q jce_policy-8.zip -d /usr/jdk64/jdk1.8.0_60/jre/lib/security/

4. Restart Ambari Server.

5. Proceed to Running the Security Wizard.

Running the Kerberos Security Wizard
____________________________________

Ambari provides three options for enabling Kerberos:

* Existing MIT KDC
* Existing Active Directory
* Manage Kerberos principals and keytabs manually

When choosing **Existing MIT KDC** or **Existing Active Directory**, the Kerberos Wizard prompts for information related to the KDC, the KDC Admin Account and the Service and Ambari principals.
Once provided, Ambari will automatically create principals, generate keytabs and distribute keytabs to the hosts in the cluster.
The services will be configured for Kerberos and the service components are restarted to authenticate against the KDC.
This is the **Automated Setup** option.

When choosing **Manage Kerberos principals and keytabs manually**, you must create the principals, generate and distribute the keytabs.
Ambari will not do this automatically.
This is the **Manual Setup** option.

Launching the Kerberos Wizard (Automated Setup)
_______________________________________________

1. Be sure you have :doc:`Installed and Configured your KDC<kdc-config>` and have :ref:`prepared the JCE<ambari-install-jce>` on each host in the cluster.

2. Log in to Ambari Web and Browse to ``Admin > Kerberos``.

3. Click “Enable Kerberos” to launch the wizard.

4. Select the type of KDC you are using and confirm you have met the prerequisites.

5. Provide information about the KDC and admin account.

  * In the **KDC** section, enter the following information:

    * In the **KDC Host** field, the IP address or FQDN for the KDC host. Optionally a port number may be included.
    * In the **Realm name** field, the default realm to use when creating service principals.
    * **Optional**: In the **Domains** field, provide a list of patterns to use to map hosts in the cluster to the appropriate realm. For example ``.yourdomain.local , yourdomain.local``.

  * In the **Kadmin** section, enter the following information:

    * In the **Kadmin** Host field, the IP address or FQDN for the KDC administrative host. Optionally a port number may be included.
    * The **Admin principal** and **password** that will be used to create principals and keytabs.

6. Modify any advanced Kerberos settings based on your environment.

  * **Optional**: To manage your Kerberos client krb5.conf manually (and not have Ambari manage the krb5.conf), expand the **Advanced krb5-conf** section and uncheck the "Manage" option. **You must have the krb5.conf configured on each host**.

    .. Note::
      When manually managing the krb5.conf it is recommended to ensure that DNS is not used for looking up KDC, and REALM entries. Relying on DNS can cause negative performance, and functional impact. To ensure that DNS is not used, ensure the following entries are set in the libdefaults section of your configuration.

      ::

        [libdefaults]
        dns_lookup_kdc = false
        dns_lookup_realm = false

  * **Optional**: to configure any additional KDC's to be used for this environment, add an entry for each additional KDC to the realms section of the Advanced krb5-conf's krb5-conf template.

    ::

      kdc = {{kdc_host}}
      kdc = otherkdc.example.com

  * **Optional**: To not have Ambari install the Kerberos client libraries on all hosts, expand the **Advanced kerberos-env** section and uncheck the “Install OS-specific Kerberos client package(s)” option. **You must have the Kerberos client utilities installed on each host**.
  * **Optional**: If your Kerberos client libraries are in non-standard path locations, expand the **Advanced kerberos-env** section and adjust the “Executable Search Paths” option.
  * **Optional**: If your KDC has a password policy, expand the **Advanced kerberos-env** section and adjust the Password options.
  * **Optional**: Ambari will test your Kerberos settings by generating a test principal and authenticating with that principal. To customize the test principal name that Ambari will use, expand the **Advanced kerberos-env** section and adjust the **Test Kerberos Principal** value. By default, the test princial name is a combination of cluster name and date **(${cluster_name}-${short_date})**. This test principal **will be deleted** after the test is complete.
  * **Optional**: If you need to customize the attributes for the principals Ambari will create, when using Active Directory, see the Customizing the Attribute Template for more information. When using MIT KDC, you can pass Principal Attributes options in the Advanced kerberos-env section. For example, you can set options related to pre-auth or max. renew life by passing:

    ::

      -requires_preauth -maxrenewlife "7 days"

7. Proceed with the install.

8. Ambari will install Kerberos clients on the hosts and test access to the KDC by testing that Ambari can create a principal, generate a keytab and distribute that keytab.

9. Customize the Kerberos identities used by |rbd-stack| and proceed to kerberize the cluster.

  .. Important::
    On the Configure Identities step, be sure to review the principal names, particularly the Ambari Principals on the General tab. These principal names, by default, append the name of the cluster to each of the Ambari principals. You can leave this as default or adjust these by removing the "-${cluster-name}" from principal name string. For example, if your cluster is named |rbd-stack| and your realm is EXAMPLE.COM, the hdfs principal will be created as hdfs-RBD@EXAMPLE.COM.

10. Confirm your configuration. You can optionally download a CSV file of the principals and keytabs that Ambari will automatically create.

11. Click Next to start the process.

12. After principals have been created and keytabs have been generated and distributed, Ambari updates the cluster configurations, then starts and tests the Services in the cluster.

13. Exit the wizard when complete.

Launching the Kerberos Wizard (Manual Setup)
____________________________________________

1. Be sure you have :doc:`Installed and Configured your KDC<kdc-config>` and have :ref:`prepared the JCE<ambari-install-jce>` on each host in the cluster.

2. Log in to Ambari Web and Browse to ``Admin > Kerberos``.

3. Click “Enable Kerberos” to launch the wizard.

4. Select the **Manage Kerberos principals and keytabs manually** option and confirm you have met the prerequisites.

5. Providing information about the KDC and your Kerberos environment. If your Kerberos client libraries are in non-standard path locations, expand the **Advanced kerberos-env** section and adjust the “Executable Search Paths” option.

6. Customize the Kerberos identities used by Hadoop and proceed to kerberize the cluster.

  .. Important::
    On the Configure Identities step, be sure to review the principal names, particularly the Ambari Principals on the General tab.
    These principal names, by default, append the name of the cluster to each of the Ambari principals.
    You can leave this as default or adjust these by removing the "-${cluster-name}" from principal name string.
    For example, if your cluster is named |rbd-stack| and your realm is EXAMPLE.COM, the hdfs principal will be created as hdfs-RBD@EXAMPLE.COM.

7. Confirm your configuration. Since you have chosen the Manual Kerberos Setup option, obtain the CSV file for the list of principals and keytabs required for the cluster to work with Kerberos. **Do not proceed until you have manually created and distributed the principals and keytabs to the cluster hosts**.

8. Click Next to continue.

9. Ambari updates the cluster configurations, then starts and tests the Services in the cluster.

10. Exit the wizard when complete.