Setting Up Hadoop Group Mapping for LDAP/AD
===========================================

To ensure that LDAP/AD group level authorization is enforced in Hadoop, you should set up Hadoop group mapping for LDAP/AD.

**Prerequisites**: Access to LDAP and the connection details. Note that LDAP settings can vary depending on what LDAP implementation you are using.

There are three ways to set up Hadoop group mapping:

* :ref:`Configuring Hadoop Group Mapping for LDAP/AD Using SSSD (Recommended)<ambari-configure-hadoop-group-sssd>`
* :ref:`Configure Hadoop Group Mapping in core-site.xml<ambari-configure-hadoop-group-coresite>`
* :ref:`Manually Create the Users and Groups in the Linux Environment<ambari-configure-hadoop-group-manually>`

.. _ambari-configure-hadoop-group-sssd:

Configure Hadoop Group Mapping for LDAP/AD Using SSSD
_____________________________________________________

The recommended method for group mapping is to use `SSSD <https://fedorahosted.org/sssd/>`_ or one of the following services to connect the Linux OS with LDAP:

* Centrify
* NSLCD
* Winbind
* SAMBA

Note that most of these services allow you to not only look up a user and enumerate their groups, but also allow you to perform other actions on the host.
None of these features are required for LDAP group mapping on Hadoop -- all that is required is the ability to lookup (or "validate") a user within LDAP and enumerate their groups.
Therefore, when evaluating these services, take the time to understand the difference between the NSS module (which performs user/group resolution) and the PAM module (which performs user authentication).
NSS is required.
PAM is not required, and may represent a security risk.

.. _ambari-configure-hadoop-group-coresite:

Configure Hadoop Group Mapping in core-site.xml
_______________________________________________

You can use the following steps to configure Hadoop to use LDAP-based group mapping in ``core-site.xml``.

1. Add the properties shown in the example below to the ``core-site.xml`` file. You will need to provide the value for the bind user, the bind password, and other properties specific to you LDAP instance, and make sure that object class, user, and group filters match the values specified in your LDAP instance.

  ::

    <property>
      <name>hadoop.security.group.mapping</name>
      <value>org.apache.hadoop.security.LdapGroupsMapping</value>
    </property>

    <property>
      <name>hadoop.security.group.mapping.ldap.bind.user</name>
      <value>cn=Manager,dc=hadoop,dc=apache,dc=org</value>
    </property>

    <!–
    <property>
      <name>hadoop.security.group.mapping.ldap.bind.password.file</name>
      <value>/etc/hadoop/conf/ldap-conn-pass.txt</value>
    </property>
    –>

    <property>
      <name>hadoop.security.group.mapping.ldap.bind.password</name>
      <value>hadoop</value>
    </property>

    <property>
      <name>hadoop.security.group.mapping.ldap.url</name>
      <value>ldap://localhost:389/dc=hadoop,dc=apache,dc=org</value>
    </property>

    <property>
      <name>hadoop.security.group.mapping.ldap.url</name>
      <value>ldap://localhost:389/dc=hadoop,dc=apache,dc=org</value>
    </property>

    <property>
      <name>hadoop.security.group.mapping.ldap.base</name>
      <value></value>
    </property>

    <property>
      <name>hadoop.security.group.mapping.ldap.search.filter.user</name>
      <value>(&amp;(|(objectclass=person)(objectclass=applicationProcess))(cn={0}))</value>
    </property>

    <property>
      <name>hadoop.security.group.mapping.ldap.search.filter.group</name>
      <value>(objectclass=groupOfNames)</value>
    </property>

    <property>
      <name>hadoop.security.group.mapping.ldap.search.attr.member</name>
      <value>member</value>
    </property>

    <property>
      <name>hadoop.security.group.mapping.ldap.search.attr.group.name</name>
      <value>cn</value>
    </property>

2. Depending on your configuration, you may be able to refresh user and group mappings using the following HDFS commands:

  ::

    hdfs dfsadmin -refreshUserToGroupsMappings

  If a restart is required, you can use the applicable instructions on :doc:`this</ambari/user-guide/manage-services>` page to re-start the HDFS NameNode.

3. Verify LDAP group mapping by running the ``hdfs groups`` command. This command will fetch groups from LDAP for the current user. Note that with LDAP group mapping configured, the HDFS permissions can leverage groups defined in LDAP for access control.

.. _ambari-configure-hadoop-group-manually:

Manually Create the Users and Groups in the Linux Environment
_____________________________________________________________

You can also `manually create users and groups <https://www.linode.com/docs/tools-reference/linux-users-and-groups>`_ in your Linux environment.