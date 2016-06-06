Managing Hosts
==============

Use Ambari Hosts to manage multiple |rbd-stack| components such as DataNodes, NameNodes, CassandraNodes and AlluxioNodes, running on hosts throughout your cluster. For example, you can restart all DataNode components, optionally controlling that task with rolling restarts. Ambari Hosts supports filtering your selection of host components, based on operating status, host health, and defined host groupings.

* :ref:`Working with Hosts<ambari-working-with-hosts>`
* :ref:`Determining Host Status<ambari-determining-host-status>`
* :ref:`Filtering the Hosts List<ambari-filtering-host-lists>`
* :ref:`Performing Host-Level Actions<ambari-performing-host-level-action>`
* :ref:`Viewing Components on a Host<ambari-viewing-host-components>`
* :ref:`Decommissioning Masters and Slaves<ambari-decommissioning-masters-slaves>`
* :ref:`How to Delete a Component<ambari-delete-component>`
* :ref:`Deleting a Host from a Cluster<ambari-delete-cluster-host>`
* :ref:`Setting Maintenance Mode<ambari-setting-maintenance-mode>`
* :ref:`Adding Hosts to a Cluster<ambari-add-cluster-host>`
* :ref:`Rack Awareness<ambari-rack-awarness>`

.. _ambari-working-with-hosts:

Working with Hosts
__________________

Use Hosts to view hosts in your cluster on which services run. Use options on Actions to perform actions on one or more hosts in your cluster.

View individual hosts, listed by fully-qualified domain name, on the Hosts landing page.

.. image:: /img/ambari/hosts_list.png

.. _ambari-determining-host-status:

Determining Host Status
_______________________

A colored dot beside each host name indicates operating status of each host, as follows:

* Red - At least one master component on that host is down. Hover to see a tooltip that lists affected components.
* Orange - At least one slave component on that host is down. Hover to see a tooltip that lists affected components.
* Yellow - Ambari Server has not received a heartbeat from that host for more than 3 minutes.
* Green - Normal running state.

A red condition flag overrides an orange condition flag, which overrides a yellow condition flag. In other words, a host having a master component down may also have other issues. The following example shows three hosts, one having a master component down, one having a slave component down, and one healthy. Warning indicators appear next to hosts having a component down.

.. image:: /img/ambari/hosts_statuses.png

.. _ambari-filtering-host-lists:

Filtering the Hosts List
________________________

Use Filters to limit listed hosts to only those having a specific operating status. The number of hosts in your cluster having a listed operating status appears after each status name, in parenthesis. For example, the following cluster has one host having healthy status and three hosts having Maintenance Mode turned on.

.. image:: /img/ambari/hosts_filter_icons.png

For example, to limit the list of hosts appearing on Hosts home to only those with Healthy status, select Filters, then choose the Healthy option. In this case, one host name appears on Hosts home. Alternatively, to limit the list of hosts appearing on Hosts home to only those having Maintenance Mode on, select Filters, then choose the Maintenance Mode option. In this case, three host names appear on Hosts home.

Use the general filter tool to apply specific search and sort criteria that limits the list of hosts appearing on the Hosts page.

.. _ambari-performing-host-level-action:

Performing Host-Level Actions
_____________________________

Use Actions to act on one, or multiple hosts in your cluster. Actions performed on multiple hosts are also known as bulk operations.

Actions comprises three menus that list the following option types:

* Hosts - lists selected, filtered or all hosts options, based on your selections made using Hosts home and Filters.
* Objects - lists component objects that match your host selection criteria.
* Operations - lists all operations available for the component objects you selected.

For example, to restart DataNodes on one host:

1. In Hosts, select a host running at least one DataNode.
2. In Actions, choose Selected ``Hosts > DataNodes > Restart``, as shown in the following image.

  .. image:: /img/ambari/Host_datanode_restart.png

3. Choose OK to confirm starting the selected operation.
4. Optionally, use Monitoring Background Operations to follow, diagnose or troubleshoot the restart operation.

.. _ambari-viewing-host-components:

Viewing Components on a Host
____________________________

To manage components running on a specific host, choose a FQDN on the Hosts page.To manage components running on a specific host, choose a FQDN on the Hosts page.

.. image:: /img/ambari/ambari_host_detail.png

Choose options in ``Host Actions``, to start, stop, restart, delete, or turn on maintenance mode for all components installed on the selected host.

Alternatively, choose action options from the drop-down menu next to an individual component on a host. The drop-down menu shows current operation status for each component.

.. _ambari-decommissioning-masters-slaves:

Decommissioning Masters and Slaves
__________________________________

Decommissioning is a process that supports removing a component from the cluster. You must decommission a master or slave running on a host before removing the component or host from service. Decommissioning helps prevent potential loss of data or service disruption. Decommissioning is available for the following component types:

* DataNodes
* NodeManagers

Decommissioning executes the following tasks:

* For DataNodes, safely replicates the HDFS data to other DataNodes in the cluster.
* For NodeManagers, stops accepting new job requests from the masters and stops the component.

**How to Decommission a Component**

To decommission a component using Ambari Web, browse Hosts to find the host FQDN on which the component resides.

Using Actions, select HostsComponent Type, then choose Decommission.

The UI shows "Decommissioning" status while steps process, then "Decommissioned" when complete.

.. _ambari-delete-component:

How to Delete a Component
_________________________

To delete a component using Ambari Web, on ``Hosts`` choose the host FQDN on which the component resides.

1. In ``Components``, find a decommissioned component.

2. Stop the component, if necessary.

  .. Note::
    A decommissioned slave component may restart in the decommissioned state.

3. For a decommissioned component, choose Delete from the component drop-down menu.

  .. Note::
    Restarting services enables Ambari to recognize and monitor the correct number of components.

  Deleting a slave component, such as a DataNode does not automatically inform a master component, such as a NameNode to remove the slave component from its exclusion list. Adding a deleted slave component back into the cluster presents the following issue; the added slave remains decommissioned from the master's perspective. Restart the master component, as a work-around.

.. _ambari-delete-cluster-host:

Deleting a Host from a Cluster
______________________________

Deleting a host removes the host from the cluster. Before deleting a host, you must complete the following prerequisites:

* Stop all components running on the host.
* Decommission any DataNodes running on the host.
* Move from the host any master components, such as NameNode or ResourceManager, running on the host.
* Turn Off Maintenance Mode, if necessary, for the host.

To delete a host from a cluster:

#. In Hosts, click on a host name.
#. On the Host-Details page, select Host Actions drop-down menu.
#. Choose Delete.

If you have not completed prerequisite steps, a warning message similar to the following one appears:

.. image:: /img/ambari/Unable_to_delete_host_msg.png

.. _ambari-setting-maintenance-mode:

Setting Maintenance Mode
________________________

Maintenance Mode supports suppressing alerts and skipping bulk operations for specific services, components and hosts in an Ambari-managed cluster. You typically turn on Maintenance Mode when performing hardware or software maintenance, changing configuration settings, troubleshooting, decommissioning, or removing cluster nodes. You may place a service, component, or host object in Maintenance Mode before you perform necessary maintenance or troubleshooting tasks.

Maintenance Mode affects a service, component, or host object in the following two ways:

* Maintenance Mode suppresses alerts, warnings and status change indicators generated for the object
* Maintenance Mode exempts an object from host-level or service-level bulk operations

Explicitly turning on Maintenance Mode for a service implicitly turns on Maintenance Mode for components and hosts that run the service. While Maintenance Mode On prevents bulk operations being performed on the service, component, or host, you may explicitly start and stop a service, component, or host having Maintenance Mode On.

**Setting Maintenance Mode for Services, Components, and Hosts**

For example, examine using Maintenance Mode in a 3-node, Ambari-managed cluster installed using default options. This cluster has one data node, on host c6403. This example describes how to explicitly turn on Maintenance Mode for the HDFS service, alternative procedures for explicitly turning on Maintenance Mode for a host, and the implicit effects of turning on Maintenance Mode for a service, a component and a host.

**How to Turn On Maintenance Mode for a Service**

#. Using Services, select ``HDFS``.
#. Select Service Actions, then choose ``Turn On Maintenance Mode``.
#. Choose OK to confirm.

  Notice, on Services Summary that Maintenance Mode turns on for the NameNode and SNameNode components.

**How to Turn On Maintenance Mode for a Host**

#. Using Hosts, select ``c6401.ambari.apache.org``.
#. Select Host Actions, then choose ``Turn On Maintenance Mode``.
#. Choose OK to confirm.

  Notice on Components, that Maintenance Mode turns on for all components.

**Maintenance Mode Use Cases**

Four common Maintenance Mode Use Cases follow:

1. You want to perform hardware, firmware, or OS maintenance on a host. You want:

  * Prevent alerts generated by all components on this host.
  * Be able to stop, start, and restart each component on the host.
  * Prevent host-level or service-level bulk operations from starting, stopping, or restarting components on this host.

  To achieve these goals, turn On Maintenance Mode explicitly for the host. Putting a host in Maintenance Mode implicitly puts all components on that host in Maintenance Mode.

2. You want to test a service configuration change. You will stop, start, and restart the service using a rolling restart to test whether restarting picks up the change. You want:

  * No alerts generated by any components in this service.
  * To prevent host-level or service-level bulk operations from starting, stopping, or restarting components in this service.

  To achieve these goals, turn on Maintenance Mode explicitly for the service. Putting a service in Maintenance Mode implicitly turns on Maintenance Mode for all components in the service.

3. You turn off a service completely. You want:

  * The service to generate no warnings.
  * To ensure that no components start, stop, or restart due to host-level actions or bulk operations.

  To achieve these goals, turn On Maintenance Mode explicitly for the service. Putting a service in Maintenance Mode implicitly turns on Maintenance Mode for all components in the service.

4. A host component is generating alerts. You want:

  * Check the component.
  * Assess warnings and alerts generated for the component.
  * Prevent alerts generated by the component while you check its condition.

To achieve these goals, turn on Maintenance Mode explicitly for the host component. Putting a host component in Maintenance Mode prevents host-level and service-level bulk operations from starting or restarting the component. You can restart the component explicitly while Maintenance Mode is on.

.. _ambari-add-cluster-host:

Adding Hosts to a Cluster
_________________________

To add new hosts to your cluster, browse to the Hosts page and select Actions >+Add New Hosts. The Add Host Wizard provides a sequence of prompts similar to those in the Ambari Install Wizard. Follow the prompts, providing information similar to that provided to define the first set of hosts in your cluster.

.. image:: /img/ambari/add-hosts.png

.. _ambari-rack-awarness:

Rack Awareness
______________

Ambari can manage Rack information for hosts. By setting the Rack ID, Ambari can display the hosts in heatmaps by Rack ID, as well users can filter & find hosts based on Rack ID on the Hosts page.

If HDFS is installed in your cluster, Ambari will pass this Rack ID information to HDFS via a topology script. Ambari generates a topology script at ``/etc/hadoop/conf/topology.py`` and sets the ``net.topology.script.file.name`` property in ``core-site`` automatically. This topology script reads a mappings file ``/etc/hadoop/conf/topology_mappings.data`` that Ambari automatically generates. When you make changes to Rack ID assignment in Ambari, this mappings file will be updated when you push out the HDFS configuration. HDFS uses this topology script to obtain Rack information about the DataNode hosts.

**Setting Rack ID**

There are two methods in Ambari Web for setting the Rack ID. You can set the Rack ID for hosts in bulk on the Hosts page using the Actions menu; and you can set the Rack ID on an individual host by viewing the Host page using the Host Actions menu.

To set the Rack ID in bulk on the Hosts page, use the Actions menu and select Hosts > Set Rack (for All, Filtered or Selected hosts).

.. image:: /img/ambari/Set_Rack.png

To set the Rack ID on an individual host, browse to the Host page, use the Host Actions menu and select Set Rack.

.. image:: /img/ambari/Set_Rack_indiv_host.png

**Using a Custom Topology Script**

It is possible to not have Ambari manage the Rack information for hosts. Instead, you can use a custom topology script to provide rack information to HDFS and not use the Ambari-generated topology.py script. If you choose to manage Rack information on your own, you will need to **create your own topology script and manage distributing the script to all hosts**. Ambari will also not have any knowledge of host Rack information so heatmaps will not display by Rack in Ambari Web.

To manage Rack information on your own, in the ``Services > HDFS > Configs``, modify the ``net.topology.script.file.name property``. Set this property value to your own custom topology script (for example ``/etc/hadoop/conf/topology.sh`` ). Distribute that topology script to your hosts and manage the Rack mapping information for your script outside of Ambari.