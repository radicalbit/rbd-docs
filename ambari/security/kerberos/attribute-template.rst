Customizing the Attribute Template
==================================

If you are using the Kerberos Automated setup with Active Directory, depending on your KDC policies, you can customize the attributes that Ambari sets when creating principals.
On the Configure Kerberos step of the wizard, in the **Advanced kerberos-env** section, you have access to the Ambari Attribute Template.
This template (which is based on the Apache Velocity templating syntax) can be modified to adjust which attributes are set on the principals and how those attribute values are derived.

The following table lists the set of computed attribute variables available if you choose to modify the template:

+-----------------------+-------------------------------------------+
| Attribute Variables   | Example                                   |
+=======================+===========================================+
| $normalized_principal | nn/c6401.ambari.apache.org@EXAMPLE.COM    |
+-----------------------+-------------------------------------------+
| $principal_name       | nn/c6401.ambari.apache.org                |
+-----------------------+-------------------------------------------+
| $principal_primary    | nn                                        |
+-----------------------+-------------------------------------------+
| $principal_digest     | [[MD5 hash of the $normalized_principal]] |
+-----------------------+-------------------------------------------+
| $principal_instance   | c6401.ambari.apache.org                   |
+-----------------------+-------------------------------------------+
| $realm                | EXAMPLE.COM                               |
+-----------------------+-------------------------------------------+
| $password             | [[password]]                              |
+-----------------------+-------------------------------------------+