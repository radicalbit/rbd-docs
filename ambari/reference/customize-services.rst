Customizing |rbd-stack| Services
================================

Defining Service Users and Groups for a |rbd-stack| Stack
_________________________________________________________

The individual services in Hadoop run under the ownership of their respective Unix accounts.
These accounts are known as service users.
These service users belong to a special Unix group.
"Smoke Test" is a service user dedicated specifically for running smoke tests on components during installation using the Services View of the Ambari Web GUI.
You can also run service checks as the "Smoke Test" user on-demand after installation.
You can customize any of these users and groups using the Misc tab during the Customize Services installation step.

.. Note::
  Use the ``Skip Group Modifications`` option to not modify the Linux groups in the cluster.
  Choosing this option is typically required if your environment manages groups using LDAP and not on the local Linux machines.

If you choose to customize names, Ambari checks to see if these custom accounts already exist.
If they do not exist, Ambari creates them. The default accounts are always created during installation whether or not custom accounts are specified.
These default accounts are not used and can be removed post-install.

.. Note::
  All new service user accounts, and any existing user accounts used as service users, must have a UID >= 1000.

Below the list of all service users and service groups:

+----------------+---------------------------------+----------------------+
| Service        | Component                       | Default User Account |
+================+=================================+======================+
| Alluxio        | | Alluxio Master                | alluxio              |
|                | | Alluxio Worker                |                      |
+----------------+---------------------------------+----------------------+
| Ambari Metrics | | Metrics Collector             | ams                  |
|                | | Metrics Monitor               |                      |
+----------------+---------------------------------+----------------------+
| Cassandra      | | Cassandra Seed                | cassandra            |
|                | | Cassandra Node                |                      |
+----------------+---------------------------------+----------------------+
| Flink          | | Flink Master                  | flink                |
+----------------+---------------------------------+----------------------+
| HDFS           | | NameNode                      | hdfs                 |
|                | | SecondaryNameNode             |                      |
|                | | DataNode                      |                      |
+----------------+---------------------------------+----------------------+
| Kafka          | | Kafka Broker                  | kafka                |
+----------------+---------------------------------+----------------------+
| PostgreSQL     | | PostgreSQL (Ambari Server)    | postgres             |
+----------------+---------------------------------+----------------------+
| YARN           | | NodeManager                   | yarn                 |
|                | | ResourceManager               |                      |
+----------------+---------------------------------+----------------------+
| Zeppelin       | | Zeppelin Notebook             | zeppelin             |
+----------------+---------------------------------+----------------------+

+---------+------------+-----------------------+
| Service | Components | Default Group Account |
+=========+============+=======================+
| All     | All        | rbp-services          |
+---------+------------+-----------------------+

For all components, the Smoke Test user performs smoke tests against cluster services as part of the install process.
It also can perform these on-demand, from the Ambari Web UI. The default user account for the smoke test user is ambari-qa.

Setting Properties That Depend on Service Usernames/Groups
__________________________________________________________

Some properties must be set to match specific service user names or service groups.
If you have set up non-default, customized service user names for the HDFS service or the |rbd-stack| group name, you must edit the following properties, using ``Services > Service.Name > Configs > Advanced``:

**HDFS Settings: Advanced**

+----------------------------------+------------------------------------------------------+
| Property Name                    | Value                                                |
+==================================+======================================================+
| dfs.permissions.superusergroup   | The same as the HDFS username. The default is "hdfs" |
+----------------------------------+------------------------------------------------------+
| dfs.cluster.administrators       | A single space followed by the HDFS username.        |
+----------------------------------+------------------------------------------------------+
