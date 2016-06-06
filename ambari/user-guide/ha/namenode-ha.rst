NameNode High Availability
==========================

To ensure that a NameNode in your cluster is always available if the primary NameNode host fails, enable and set up NameNode High Availability on your cluster using Ambari Web.

How To Configure NameNode High Availability
___________________________________________

1. Check to make sure you have at least three hosts in your cluster and are running at least three ZooKeeper servers.

2. Check to make sure that the HDFS and ZooKeeper services are not in Maintenance Mode.

  These services will be stopped and started when enabling NameNode HA. Maintenance Mode will prevent those start and stop operations from occurring. If the HDFS or ZooKeeper services are in Maintenance Mode the NameNode HA wizard will not complete successfully.

3. In Ambari Web, select ``Services > HDFS > Summary``.

4. Select ``Service Actions`` and choose ``Enable NameNode HA``.

5. The Enable HA Wizard launches. This wizard describes the set of automated and manual steps you must take to set up NameNode high availability.

6. **Get Started** : This step gives you an overview of the process and allows you to select a Nameservice ID. You use this Nameservice ID instead of the NameNode FQDN once HA has been set up. Click Next to proceed.

  .. image:: /img/ambari/getstartedHA_2x.png

7. **Select Hosts** : Select a host for the additional NameNode and the JournalNodes. The wizard suggest options that you can adjust using the drop-down lists. Click Next to proceed.

  .. image:: /img/ambari/selecthostha_2x.png

8. **Review** : Confirm your host selections and click Next.

  .. image:: /img/ambari/reviewha_2x.png

9. **Create Checkpoints** : Follow the instructions in the step. You need to log in to your current NameNode host to run the commands to put your NameNode into safe mode and create a checkpoint. When Ambari detects success, the message on the bottom of the window changes. Click Next.

  .. image:: /img/ambari/checkpointsHA_2x.png

10. **Configure Components** : The wizard configures your components, displaying progress bars to let you track the steps. Click Next to continue.

  .. image:: /img/ambari/configurecomponentsHA_2x.png

11. **Initialize JournalNodes** : Follow the instructions in the step. You need to login to your current NameNode host to run the command to initialize the JournalNodes. When Ambari detects success, the message on the bottom of the window changes. Click Next.

  .. image:: /img/ambari/initializejournalnodesHA_2x.png

12. **Start Components** : The wizard starts the ZooKeeper servers and the NameNode, displaying progress bars to let you track the steps. Click Next to continue.

  .. image:: /img/ambari/startcomponentsHA_2x.png

13. **Initialize Metadata** : Follow the instructions in the step. For this step you must log in to both the current NameNode and the additional NameNode. Make sure you are logged in to the correct host for each command. Click Next when you have completed the two commands. A Confirmation pop-up window displays, reminding you to do both steps. Click OK to confirm.

  .. image:: /img/ambari/initializemetadataHA_2x.png

14. **Finalize HA Setup** : The wizard the setup, displaying progress bars to let you track the steps. Click Done to finish the wizard. After the Ambari Web GUI reloads, you may see some alert notifications. Wait a few minutes until the services come back up. If necessary, restart any components using Ambari Web.

  .. image:: /img/ambari/finalizeHA_2x.png

15. Adjust the ZooKeeper Failover Controller retries setting for your environment.

  * Browse to ``Services > HDFS > Configs > Advanced core-site``.
  * Set ``ha.failover-controller.active-standby-elector.zk.op.retries=120``

How to Roll Back NameNode HA
____________________________

To roll back NameNode HA to the previous non-HA state use the following step-by-step manual process:

#. :ref:`Checkpoint the Active NameNode<ambari-checkpoint-namenode>`
#. :ref:`Stop All Services<ambari-namenode-ha-stop-all-services>`
#. :ref:`Prepare the Ambari Host for Rollback<ambari-prepare-host-rollback>`
#. :ref:`Delete ZooKeeper Failover Controllers<ambari-delete-zkfcontrollers>`
#. :ref:`Modify HDFS Configurations<ambari-modify-hdfs-config>`
#. :ref:`Recreate the standby NameNode<ambari-recreate-namenode>`
#. :ref:`Re-enable the standby NameNode<ambari-reenable-namenode>`
#. :ref:`Delete All JournalNodes<ambari-delete-journalnode>`
#. :ref:`Delete the Additional NameNode<ambari-delete-namenode>`
#. :ref:`Verify the HDFS Components<ambari-verify-hdfs>`
#. :ref:`Start HDFS<ambari-start-hdfs>`

.. _ambari-checkpoint-namenode:

**Checkpoint the Active NameNode**

If HDFS has been in use after you enabled NameNode HA, but you wish to revert back to a non-HA state, you must checkpoint the HDFS state before proceeding with the rollback.

If the ``Enable NameNode HA`` wizard failed and you need to revert back, you can skip this step and move on to :ref:`Stop All Services<ambari-namenode-ha-stop-all-services>`.

* If Kerberos security has not been enabled on the cluster:

  On the Active NameNode host, execute the following commands to save the namespace. You must be the HDFS service user to do this.

  ::

    sudo su -l <HDFS_USER> -c 'hdfs dfsadmin -safemode enter' sudo su -l <HDFS_USER> -c 'hdfs dfsadmin -saveNamespace'

* If Kerberos security has been enabled on the cluster:

  ::

    sudo su -l <HDFS_USER> -c 'kinit -kt /etc/security/keytabs/nn.service.keytab nn/<HOSTNAME>@<REALM>;hdfs dfsadmin -safemode enter' sudo su -l <HDFS_USER> -c 'kinit -kt /etc/security/keytabs/nn.service.keytab nn/<HOSTNAME>@<REALM>;hdfs dfsadmin -saveNamespace'

  Where <HDFS_USER> is the HDFS service user; for example hdfs, <HOSTNAME> is the Active NameNode hostname, and <REALM> is your Kerberos realm.

.. _ambari-namenode-ha-stop-all-services:

**Stop All Services**

Browse to ``Ambari Web > Services``, then choose ``Stop All`` in the Services navigation panel. You must wait until all the services are completely stopped.

.. _ambari-prepare-host-rollback:

**Prepare the Ambari Host for Rollback**

Log into the Ambari server host and set the following environment variables to prepare for the rollback procedure:

+--------------------------------------------------+--------------------------------------------------------------------------------+
| Variable                                         | Value                                                                          |
+==================================================+================================================================================+
| export AMBARI_USER=AMBARI_USERNAME               | Substitute the value of the administrative user for Ambari Web. The default    |
|                                                  | value is admin.                                                                |
+--------------------------------------------------+--------------------------------------------------------------------------------+
| export AMBARI_PW=AMBARI_PASSWORD                 | Substitute the value of the administrative password for Ambari Web.            |
|                                                  | The default value is admin.                                                    |
+--------------------------------------------------+--------------------------------------------------------------------------------+
| export AMBARI_PORT=AMBARI_PORT                   | Substitute the Ambari Web port. The default value is 8080.                     |
+--------------------------------------------------+--------------------------------------------------------------------------------+
| export AMBARI_PROTO=AMBARI_PROTOCOL              | Substitute the value of the protocol for connecting to Ambari Web. Options     |
|                                                  | are http or https. The default value is http.                                  |
+--------------------------------------------------+--------------------------------------------------------------------------------+
| export CLUSTER_NAME=CLUSTER_NAME                 | Substitute the name of your cluster, set during the Ambari Install Wizard      |
|                                                  | process. For example: mycluster.                                               |
+--------------------------------------------------+--------------------------------------------------------------------------------+
| export NAMENODE_HOSTNAME=NN_HOSTNAME             | Substitute the FQDN of the host for the non-HA NameNode. For example:          |
|                                                  | nn01.mycompany.com.                                                            |
+--------------------------------------------------+--------------------------------------------------------------------------------+
| export ADDITIONAL_NAMENODE_HOSTNAME=ANN_HOSTNAME | Substitute the FQDN of the host for the additional NameNode in your HA setup.  |
+--------------------------------------------------+--------------------------------------------------------------------------------+
| export SECONDARY_NAMENODE_HOSTNAME=SNN_HOSTNAME  | Substitute the FQDN of the host for the standby NameNode for the non-HA setup. |
+--------------------------------------------------+--------------------------------------------------------------------------------+
| export JOURNALNODE1_HOSTNAME=JOUR1_HOSTNAME      | Substitute the FQDN of the host for the first Journal Node.                    |
+--------------------------------------------------+--------------------------------------------------------------------------------+
| export JOURNALNODE2_HOSTNAME=JOUR2_HOSTNAME      | Substitute the FQDN of the host for the second Journal Node.                   |
+--------------------------------------------------+--------------------------------------------------------------------------------+
| export JOURNALNODE3_HOSTNAME=JOUR3_HOSTNAME      | Substitute the FQDN of the host for the third Journal Node.                    |
+--------------------------------------------------+--------------------------------------------------------------------------------+

Double check that these environment variables are set correctly.

.. _ambari-delete-zkfcontrollers:

**Delete ZooKeeper Failover Controllers**

You may need to delete ZooKeeper (ZK) Failover Controllers.

1. To check if you need to delete ZK Failover Controllers, on the Ambari Server host:

  ::

    curl -u <AMBARI_USER>:<AMBARI_PW> -H "X-Requested-By: ambari" -i <AMBARI_PROTO>://localhost:<AMBARI_PORT>/api/v1/clusters/<CLUSTER_NAME>/host_components?HostRoles/component_name=ZKFC

  If this returns an empty items array, you may proceed to :ref:`Modify HDFS Configuration<ambari-modify-hdfs-config>`. Otherwise you must use the following DELETE commands:

2. To delete all ZK Failover Controllers, on the Ambari Server host:

  ::

    curl -u <AMBARI_USER>:<AMBARI_PW> -H "X-Requested-By: ambari" -i -X DELETE <AMBARI_PROTO>://localhost:<AMBARI_PORT>/api/v1/clusters/<CLUSTER_NAME>/hosts/<NAMENODE_HOSTNAME>/host_components/ZKFC curl -u <AMBARI_USER>:<AMBARI_PW> -H "X-Requested-By: ambari" -i -X DELETE <AMBARI_PROTO>://localhost:<AMBARI_PORT>/api/v1/clusters/<CLUSTER_NAME>/hosts/<ADDITIONAL_NAMENODE_HOSTNAME>/host_components/ZKFC

3. Verify that the ZK Failover Controllers have been deleted. On the Ambari Server host:

  ::

    curl -u <AMBARI_USER>:<AMBARI_PW> -H "X-Requested-By: ambari" -i <AMBARI_PROTO>://localhost:<AMBARI_PORT>/api/v1/clusters/<CLUSTER_NAME>/host_components?HostRoles/component_name=ZKFC

  This command should return an empty items array.

.. _ambari-modify-hdfs-config:

**Modify HDFS Configurations**

You may need to modify your ``hdfs-site`` configuration and/or your ``core-site`` configuration.

1. To check if you need to modify your hdfs-site configuration, on the Ambari Server host:

  ::

    /var/lib/ambari-server/resources/scripts/configs.sh -u <AMBARI_USER> \
        -p <AMBARI_PW> \
        -port <AMBARI_PORT> \
        get localhost <CLUSTER_NAME> hdfs-site

  If you see **any** of the following properties, you must delete them from your configuration.

  * ``dfs.nameservices``
  * ``dfs.client.failover.proxy.provider.<NAMESERVICE_ID>``
  * ``dfs.ha.namenodes.<NAMESERVICE_ID>``
  * ``dfs.ha.fencing.methods``
  * ``dfs.ha.automatic-failover.enabled``
  * ``dfs.namenode.http-address.<NAMESERVICE_ID>.nn1``
  * ``dfs.namenode.http-address.<NAMESERVICE_ID>.nn2``
  * ``dfs.namenode.rpc-address.<NAMESERVICE_ID>.nn1``
  * ``dfs.namenode.rpc-address.<NAMESERVICE_ID>.nn2``
  * ``dfs.namenode.shared.edits.dir``
  * ``dfs.journalnode.edits.dir``
  * ``dfs.journalnode.http-address``
  * ``dfs.journalnode.kerberos.internal.spnego.principal``
  * ``dfs.journalnode.kerberos.principal``
  * ``dfs.journalnode.keytab.file``

  Where <NAMESERVICE_ID> is the NameService ID you created when you ran the Enable NameNode HA wizard.

2. To delete these properties, execute the following for **each** property you found. On the Ambari Server host:

  ::

    /var/lib/ambari-server/resources/scripts/configs.sh -u <AMBARI_USER> \
          -p <AMBARI_PW> \
          -port <AMBARI_PORT> \
          delete localhost <CLUSTER_NAME> hdfs-site property_name

  Where you replace ``property_name`` with the name of **each** of the properties to be deleted.

3. Verify that all of the properties have been deleted. On the Ambari Server host:

  ::

    /var/lib/ambari-server/resources/scripts/configs.sh -u <AMBARI_USER> \
        -p <AMBARI_PW> \
        -port <AMBARI_PORT> \
        get localhost <CLUSTER_NAME> hdfs-site

  None of the properties listed above should be present.

4. To check if you need to modify your core-site configuration, on the Ambari Server host:

  ::

    /var/lib/ambari-server/resources/scripts/configs.sh -u <AMBARI_USER> \
        -p <AMBARI_PW>  \
        -port <AMBARI_PORT> \
        get localhost <CLUSTER_NAME> core-site

5. If you see the property ``ha.zookeeper.quorum``, it must be deleted. On the Ambari Server host:

  ::

    /var/lib/ambari-server/resources/scripts/configs.sh -u <AMBARI_USER> \
        -p <AMBARI_PW> \
        -port <AMBARI_PORT> \
        delete localhost <CLUSTER_NAME> core-site ha.zookeeper.quorum

6. If the property ``fs.defaultFS`` is set to the NameService ID, it must be reverted back to its non-HA value.

7. To revert the property fs.defaultFS to the NameNode host value, on the Ambari Server host:

  ::

    /var/lib/ambari-server/resources/scripts/configs.sh -u <AMBARI_USER> \
        -p <AMBARI_PW> \
        -port <AMBARI_PORT> \
        set localhost <CLUSTER_NAME> core-site fs.defaultFS hdfs://<NAMENODE_HOSTNAME>

8. Verify that the core-site properties are now properly set. On the Ambari Server host:

  ::

    /var/lib/ambari-server/resources/scripts/configs.sh -u <AMBARI_USER> \
        -p <AMBARI_PW> \
        -port <AMBARI_PORT> \
        get localhost <CLUSTER_NAME> core-site

  The property ``fs.defaultFS`` should be set to point to the NameNode host and the property ``ha.zookeeper.quorum`` should not be there.

.. _ambari-recreate-namenode:

**Recreate the standby NameNode**

You may need to recreate your standby NameNode.

1. To check to see if you need to recreate the standby NameNode, on the Ambari Server host:

  ::

    curl -u <AMBARI_USER>:<AMBARI_PW> -H "X-Requested-By: ambari" -i -X GET <AMBARI_PROTO>://localhost:<AMBARI_PORT>/api/v1/clusters/<CLUSTER_NAME>/host_components?HostRoles/component_name=SECONDARY_NAMENODE

  If this returns an empty items array, you must recreate your standby NameNode. Otherwise you can go on to Re-enable Standby NameNode.

2. Recreate your standby NameNode. On the Ambari Server host:

  ::

    curl -u <AMBARI_USER>:<AMBARI_PW> -H "X-Requested-By: ambari" -i -X POST -d '{"host_components" : [{"HostRoles":{"component_name":"SECONDARY_NAMENODE"}] }' <AMBARI_PROTO>://localhost:<AMBARI_PORT>/api/v1/clusters/<CLUSTER_NAME>/hosts?Hosts/host_name=<SECONDARY_NAMENODE_HOSTNAME>

3. Verify that the standby NameNode now exists. On the Ambari Server host:

  ::

    curl -u <AMBARI_USER>:<AMBARI_PW> -H "X-Requested-By: ambari" -i -X GET <AMBARI_PROTO>://localhost:<AMBARI_PORT>/api/v1/clusters/<CLUSTER_NAME>/host_components?HostRoles/component_name=SECONDARY_NAMENODE

  This should return a non-empty items array containing the standby NameNode.

.. _ambari-reenable-namenode:

**Re-enable the standby NameNode**

To re-enable the standby NameNode, on the Ambari Server host:

  ::

    curl -u <AMBARI_USER>:<AMBARI_PW> -H "X-Requested-By: ambari" -i -X '{"RequestInfo":{"context":"Enable Secondary NameNode"},"Body":{"HostRoles":{"state":"INSTALLED"}}}'<AMBARI_PROTO>://localhost:<AMBARI_PORT>/api/v1/clusters/<CLUSTER_NAME>/hosts/<SECONDARY_NAMENODE_HOSTNAME}/host_components/SECONDARY_NAMENODE

* If this returns 200, go to :ref:`Delete All JournalNodes<ambari-delete-journalnode>`.
* If this returns 202, wait a few minutes and run the following command on the Ambari Server host:

  ::

    curl -u <AMBARI_USER>:${AMBARI_PW -H "X-Requested-By: ambari" -i -X "<AMBARI_PROTO>://localhost:<AMBARI_PORT>/api/v1/clusters/<CLUSTER_NAME>/host_components?HostRoles/component_name=SECONDARY_NAMENODE&fields=HostRoles/state"

  When ``"state" : "INSTALLED"`` is in the response, go on to the next step.

.. _ambari-delete-journalnode:

**Delete All JournalNodes**

You may need to delete any JournalNodes.

1. To check to see if you need to delete JournalNodes, on the Ambari Server host:

  ::

    curl -u <AMBARI_USER>:<AMBARI_PW> -H "X-Requested-By: ambari" -i -X GET <AMBARI_PROTO>://localhost:<AMBARI_PORT>/api/v1/clusters/<CLUSTER_NAME>/host_components?HostRoles/component_name=JOURNALNODE

  If this returns an empty items array, you can go on to :ref:`Delete the Additional NameNode<ambari-delete-namenode>`. Otherwise you must delete the JournalNodes.

2. To delete the JournalNodes, on the Ambari Server host:

  ::

    curl -u <AMBARI_USER>:<AMBARI_PW> -H "X-Requested-By: ambari" -i -X DELETE <AMBARI_PROTO>://localhost:<AMBARI_PORT>/api/v1/clusters/<CLUSTER_NAME>/hosts/<JOURNALNODE1_HOSTNAME>/host_components/JOURNALNODE
    curl -u <AMBARI_USER>:<AMBARI_PW> -H "X-Requested-By: ambari" -i -X DELETE <AMBARI_PROTO>://localhost:<AMBARI_PORT>/api/v1/clusters/<CLUSTER_NAME>/hosts/<JOURNALNODE2_HOSTNAME>/host_components/JOURNALNODE 
    curl -u <AMBARI_USER>:<AMBARI_PW> -H "X-Requested-By: ambari" -i -X DELETE <AMBARI_PROTO>://localhost:<AMBARI_PORT>/api/v1/clusters/<CLUSTER_NAME>/hosts/<JOURNALNODE3_HOSTNAME>/host_components/JOURNALNODE

3. Verify that all the JournalNodes have been deleted. On the Ambari Server host:

  ::

    curl -u <AMBARI_USER>:<AMBARI_PW> -H "X-Requested-By: ambari" -i -X GET <AMBARI_PROTO>://localhost:<AMBARI_PORT>/api/v1/clusters/<CLUSTER_NAME>/host_components?HostRoles/component_name=JOURNALNODE

  This should return an empty items array.

.. _ambari-delete-namenode:

**Delete the Additional NameNode**

You may need to delete your Additional NameNode.

1. To check to see if you need to delete your Additional NameNode, on the Ambari Server host:

  ::

    curl -u <AMBARI_USER>:<AMBARI_PW> -H "X-Requested-By: ambari" -i -X GET <AMBARI_PROTO>://localhost:<AMBARI_PORT>/api/v1/clusters/<CLUSTER_NAME>/host_components?HostRoles/component_name=NAMENODE

  If the items array contains two NameNodes, the Additional NameNode must be deleted.

2. To delete the Additional NameNode that was set up for HA, on the Ambari Server host:

  ::

    curl -u <AMBARI_USER>:<AMBARI_PW> -H "X-Requested-By: ambari" -i -X DELETE <AMBARI_PROTO>://localhost:<AMBARI_PORT>/api/v1/clusters/<CLUSTER_NAME>/hosts/<ADDITIONAL_NAMENODE_HOSTNAME>/host_components/NAMENODE

3. Verify that the Additional NameNode has been deleted:

  ::

    curl -u <AMBARI_USER>:<AMBARI_PW> -H "X-Requested-By: ambari" -i -X GET <AMBARI_PROTO>://localhost:<AMBARI_PORT>/api/v1/clusters/<CLUSTER_NAME>/host_components?HostRoles/component_name=NAMENODE

  This should return an items array that shows only one NameNode.

.. _ambari-verify-hdfs:

**Verify the HDFS Components**

Make sure you have the correct components showing in HDFS.

#. Go to ``Ambari Web UI > Services``, then select HDFS.
#. Check the Summary panel and make sure that the first three lines look like this:

  * NameNode
  * SNameNode
  * DataNodes

  You should **not** see any line for JournalNodes.

.. _ambari-start-hdfs:

**Start HDFS**

1. In the ``Ambari Web UI``, select ``Service Actions``, then choose ``Start``.

  Wait until the progress bar shows that the service has completely started and has passed the service checks.

  If HDFS does not start, you may need to repeat the previous step.

2. To start all of the other services, select ``Actions > Start All`` in the ``Services`` navigation panel.
