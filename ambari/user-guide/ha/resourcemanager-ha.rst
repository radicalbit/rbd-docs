ResourceManager High Availability
=================================

The following topic explains How to Configure ResourceManager High Availability.

How to Configure ResourceManager High Availability
__________________________________________________

1. Check to make sure you have at least three hosts in your cluster and are running at least three ZooKeeper servers.

2. In Ambari Web, browse to ``Services > YARN > Summary``. Select ``Service Action``s and choose ``Enable ResourceManager HA``.

3. The Enable ResourceManager HA Wizard launches. The wizard describes a set of automated and manual steps you must take to set up ResourceManager High Availability.

4. **Get Started**: This step gives you an overview of enabling ResourceManager HA. Click Next to proceed.

  .. image:: /img/ambari/RMHA-01_get_started.png

5. **Select Host**: The wizard shows you the host on which the current ResourceManager is installed and suggests a default host on which to install an additional ResourceManager. Accept the default selection, or choose an available host. Click Next to proceed.

  .. image:: /img/ambari/RMHA-02_Select_Host.png

6. **Review Selections**: The wizard shows you the host selections and configuration changes that will occur to enable ResourceManager HA. Expand YARN, if necessary, to review all the YARN configuration changes. Click Next to approve the changes and start automatically configuring ResourceManager HA.

  .. image:: /img/ambari/RMHA-03_Review.png

7. **Configure Components**: The wizard configures your components automatically, displaying progress bars to let you track the steps. After all progress bars complete, click Complete to finish the wizard.

  .. image:: /img/ambari/RMHA-04_Configure_Components.png

How to Disable ResourceManager High Availability
________________________________________________

Use the following instructions to disable ResourceManager High Availability. You will be deleting one ResourceManager and keeping one ResourceManager. This requires using the Ambari API to modify the cluster configuration to delete the ResourceManager and using the ZooKeeper client to update the znode permissions.

.. Important::
  These steps involve using the Ambari REST API. Be sure to test and verify these steps in a test environment prior to executing against a production environment.

1. In Ambari Web, stop YARN and ZooKeeper services.

2. On the Ambari Server host, use the Ambari API to retrieve the YARN configurations into a JSON file. For example, yarn-site.json.

  ::

    /var/lib/ambari-server/resources/scripts/configs.sh get ambari.server cluster.name yarn-site yarn-site.json

  where ambari.server is the hostname of your Ambari Server and cluster.name is the name of your cluster.

3. Modify the following priorities in the ``yarn-site.json`` file:

  +---------------------------------------------------------+----------------------------+
  | Property                                                | Value                      |
  +=========================================================+============================+
  | yarn.resourcemanager.ha.enabled                         | Change the value to false. |
  +---------------------------------------------------------+----------------------------+
  | yarn.resourcemanager.ha.rm-ids                          | Delete this property.      |
  +---------------------------------------------------------+----------------------------+
  | yarn.resourcemanager.hostname.rm1                       | Delete this property.      |
  +---------------------------------------------------------+----------------------------+
  | yarn.resourcemanager.hostname.rm2                       | Delete this property.      |
  +---------------------------------------------------------+----------------------------+
  | yarn.resourcemanager.webapp.address.rm1                 | Delete this property.      |
  +---------------------------------------------------------+----------------------------+
  | yarn.resourcemanager.webapp.address.rm2                 | Delete this property.      |
  +---------------------------------------------------------+----------------------------+
  | yarn.resourcemanager.webapp.https.address.rm1           | Delete this property.      |
  +---------------------------------------------------------+----------------------------+
  | yarn.resourcemanager.webapp.https.address.rm2           | Delete this property.      |
  +---------------------------------------------------------+----------------------------+
  | yarn.resourcemanager.cluster-id                         | Delete this property.      |
  +---------------------------------------------------------+----------------------------+
  | yarn.resourcemanager.ha.automatic-failover.zk-base-path | Delete this property.      |
  +---------------------------------------------------------+----------------------------+

4. Verify the following properties in the ``yarn-site.json`` file are set to the ResourceManager hostname you will be keeping:

  +-----------------------------------------------+----------------------------+
  | Property                                      | Value                      |
  +===============================================+============================+
  | yarn.resourcemanager.hostname                 | <ResourceManager hostname> |
  +-----------------------------------------------+----------------------------+
  | yarn.resourcemanager.admin.address            | <ResourceManager hostname> |
  +-----------------------------------------------+----------------------------+
  | yarn.resourcemanager.webapp.address           | <ResourceManager hostname> |
  +-----------------------------------------------+----------------------------+
  | yarn.resourcemanager.resource-tracker.address | <ResourceManager hostname> |
  +-----------------------------------------------+----------------------------+
  | yarn.resourcemanager.scheduler.address        | <ResourceManager hostname> |
  +-----------------------------------------------+----------------------------+
  | yarn.resourcemanager.webapp.https.address     | <ResourceManager hostname> |
  +-----------------------------------------------+----------------------------+
  | yarn.timeline-service.webapp.address          | <ResourceManager hostname> |
  +-----------------------------------------------+----------------------------+
  | yarn.timeline-service.webapp.https.address    | <ResourceManager hostname> |
  +-----------------------------------------------+----------------------------+
  | yarn.timeline-service.address                 | <ResourceManager hostname> |
  +-----------------------------------------------+----------------------------+
  | yarn.log.server.url                           | <ResourceManager hostname> |
  +-----------------------------------------------+----------------------------+

5. Search the ``yarn-site.json`` file and remove any references to the ResourceManager hostname that you will be removing.

6. Search the ``yarn-site.json`` file and remove any properties that might still be set for ResourceManager IDs. For example, rm1 and rm2.

7. Save the ``yarn-site.json`` file and set that configuration against the Ambari Server.

  ::

    /var/lib/ambari-server/resources/scripts/configs.sh set ambari.server cluster.name yarn-site yarn-site.json

  where ambari.server is the hostname of your Ambari Server and cluster.name is the name of your cluster.

8. Using the Ambari API, delete the ResourceManager host component for the host that you are deleting:

  ::

    curl --user admin:admin -i -H "X-Requested-By: ambari" -X DELETE http://ambari.server:8080/api/v1/clusters/cluster.name/hosts/hostname/host_components/RESOURCEMANAGER

  where ambari.server is the hostname of your Ambari Server and cluster.name is the name of your cluster and hostname is the hostname of the ResourceManager you are deleting.

9. In Ambari Web, start the ZooKeeper service. On a host that has the ZooKeeper client installed, use the ZooKeeper client to change znode permissions:

  ::

    /usr/lib/zookeeper/bin/zkCli.sh
    getAcl /rmstore/ZKRMStateRoot
    setAcl /rmstore/ZKRMStateRoot world:anyone:rwcda

10. In Ambari Web, restart ZooKeeper service and start YARN service.