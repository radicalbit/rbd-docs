Managing Services
=================

Use ``Services`` to monitor and manage selected services running in your |rbd-stack| cluster.

All services installed in your cluster are listed in the leftmost ``Services`` panel.

.. image:: /img/ambari/yarn_dashboard.png

Services supports the following tasks:

* :ref:`Starting and Stopping All Services<ambari-start-stop-services>`
* :ref:`Selecting a Service<ambari-select-service>`
* :ref:`Editing Service Config Properties<ambari-edit-service-config>`
* :ref:`Performing Service Actions<ambari-perform-service-action>`
* :ref:`Viewing Summary, Alert, and Health Information<ambari-service-summary-alerts>`
* :ref:`Rolling Restarts<ambari-rolling-restart>`
* :ref:`Refreshing YARN Capacity Scheduler<ambari-yarn-capacity-scheduler>`
* :ref:`Rebalancing HDFS<ambari-rebalancing-hdfs>`

.. _ambari-start-stop-services:

Starting and Stopping All Services
__________________________________

To start or stop all listed services at once, select ``Actions``, then choose ``Start All`` or ``Stop All``, as shown in the following example:

.. image:: /img/ambari/services_stop_all.png

.. _ambari-select-service:

Selecting a Service
___________________

Selecting a service name from the list shows current summary, alert, and health information for the selected service. To refresh the monitoring panels and show information about a different service, select a different service name from the list.

Notice the colored dot next to each service name, indicating service operating status and a small, red, numbered rectangle indicating any alerts generated for the service.

Adding a Service
________________

The Ambari install wizard installs all available |rbd-stack| services by default. You may choose to deploy only some services initially, then add other services at later times. For example, many customers deploy only core Hadoop services initially. ``Add Service`` supports deploying additional services without interrupting operations in your |fdd| cluster. When you have deployed all available services, ``Add Service`` displays disabled.

To add a service, select ``Actions > Add Service``, then complete the following procedure using the Add Service Wizard.

.. _ambari-edit-service-config:

Editing Service Config Properties
_________________________________

Select a service, then select ``Configs`` to view and update configuration properties for the selected service. For example, select Zeppelin, then select Configs. Expand a config category to view configurable service properties. For example, select Advanced zeppelin-site to configure the default server port.

.. image:: /img/ambari/zeppelin_configs.png

.. _ambari-service-summary-alerts:

Viewing Service Summary and Alerts
__________________________________

After you select a service, the ``Summary`` tab displays basic information about the selected service.

.. image:: /img/ambari/Services_Summary_hi.png

Select one of the ``View Host`` links, as shown in the following example, to view components and the host on which the selected service is running.

.. image:: /img/ambari/view_hosts_links.png

**Alerts and Health Checks**

On each Service page, in the Summary area, click Alerts to see a list of all health checks and their status for the selected service. Critical alerts are shown first. Click the text title of each alert message in the list to see the alert definition.

.. image:: /img/ambari/zookeeper_alerts.png

.. _ambari-modify-service-dashboard:

**Modifying the Service Dashboard**

Depending on the Service, the Summary tab includes a Metrics section which is by default populated with important service metrics to monitor.

This section of Metrics is customizable. You can add and remove widgets from the Dashboard as well as create new widgets. Widgets can be private only to you and your dashboard or shared in a Widget Browser library for other Ambari users to add/remove the widget from their Dashboard.

.. Important::
  You must have the Ambari Metrics service installed to be able to view, create, and customize the Service Dashboard. Only HDFS and YARN have customizable service dashboards.

**Adding or Removing a Widget**

1. Click on the “ + ” to launch the Widget Browser. Alternatively, you can choose the Actions menu in the Metrics header to Browse Widgets.

2. The Widget Browser displays the available widgets to add to your Service Dashboard. This is a combination of shared widgets and widgets you have created. Widgets that are shared are identified by the icon highlighted in the following example.

  .. image:: /img/ambari/widget_browser.png

3. If you want to only display the widgets you have created, click the “Show only my widgets” checkbox to filter the Widget Browser.

4. If a widget is already added to your dashboard, it is shown as Added. Click to remove.

5. If a widget is not already added, you can click Add.

**Creating a Widget**

#. Click on the “ + ” to launch the Widget Browser. Click the Create Widget button. Alternatively, you can choose the Actions menu in the Metrics header to Create Widget. This launches the Create Widget wizard.
#. Select the type of widget to create.
#. Depending on the service and type of widget, you can select metrics and use operators to create an Expression that will be displayed in the widget. A preview of the widget is displayed as you build the expression.
#. Enter the widget name and description. Optionally choose to Share the widget. Sharing the widget makes the widget available to all Ambari users for this cluster. Once a widget is shared, other Ambari Admins or Cluster Operators can modify or delete the widget. This cannot be undone.

**Deleting a Widget**

1. Click on the “ + ” to launch the Widget Browser. Alternatively, you can choose the Actions menu in the Metrics header to Browse Widgets.

2. The Widget Browser displays the available widgets to add to your Service Dashboard. This is a combination of shared widgets and widgets you have created. Widgets that are shared are identified by the icon highlighted in the following example.

  .. image:: /img/ambari/widget_browser.png

3. If a widget is already added to your dashboard, it is shown as Added. Click to remove.

4. For widgets that you created, you can select the More… option to delete.

5. For widgets that are shared, if you are an Ambari Admin or Cluster Operator, you will also have the option to delete.

6. Deleting a shared widget removes the widget from all users. This cannot be undone.

**Export Widget Graph Data**

You can export the metrics data from widget graphs using the Export capability. This capability is available for graph-type widgets.

#. Mouse over the widget graph. You will see an Export icon. Alternatively, if you click on the widget graph to zoom into the graph, the Export icon is present in the upper-right of the dialog.
#. Click on the Export icon. You can choose to export in CSV or JSON format.
#. Select the format and the download will begin.

**Setting Display Timezone**

You can set the timezone used for displaying metrics data in widget graphs.

#. In Ambari Web, click on your user name and select Settings.
#. In the Locale section, select the Timezone.
#. Click Save.

The Ambari Web UI will reload and graphs will be displayed using the timezone you have set.

.. _ambari-perform-service-action:

Performing Service Actions
__________________________

Manage a selected service on your cluster by performing service actions. In ``Services``, select the ``Service Actions`` drop-down menu, then choose an option. Available options depend on the service you have selected. For example, HDFS service action options include:

.. image:: /img/ambari/Service_Actions_DataNode.png

Optionally, choose ``Turn On Maintenance Mode`` to suppress alerts generated by a service before performing a service action. Maintenance Mode suppresses alerts and status indicator changes generated by the service, while allowing you to start, stop, restart, move, or perform maintenance tasks on the service. For more information about how Maintenance Mode affects bulk operations for host components, see :ref:`Setting Maintenance Mode<ambari-setting-maintenance-mode>`.

.. _ambari-monitor-backgroud-operations:

Monitoring Background Operations
________________________________

Optionally, use Background Operations to monitor progress and completion of bulk operations such as rolling restarts.

Background Operations opens by default when you run a job that executes bulk operations.

1. Select the right-arrow for each operation to show restart operation progress on each host.

  .. image:: /img/ambari/background_op_1.png

2. After restarts complete, Select the right-arrow, or a host name, to view log files and any error messages generated on the selected host.

  .. image:: /img/ambari/background_op_2.png

3. Select links at the upper-right to copy or open text files containing log and error information.

  .. image:: /img/ambari/background_op_3.png

Optionally, select the option to not show the bulk operations dialog.

Using Quick Links
_________________

Select Quick Links options to access additional sources of information about a selected service. For example, HDFS Quick Links options include the native NameNode GUI, NameNode logs, the NameNode JMX output, and thread stacks for the HDFS service. Quick Links are not available for every service.

.. image:: /img/ambari/quicklinks.png

.. _ambari-rolling-restart:

Rolling Restarts
________________

When you restart multiple services, components, or hosts, use rolling restarts to distribute the task. A rolling restart stops, then starts multiple, running slave components such as DataNodes, NodeManagers, RegionServers, or Supervisors, using a batch sequence. You set rolling restart parameter values to control the number of, time between, tolerance for failures, and limits for restarts of many components across large clusters.

To run a rolling restart:

#. Select a Service, then link to a lists of specific components or hosts that Require Restart.
#. Select Restart, then choose a slave component option.
#. Review and set values for Rolling Restart Parameters.
#. Optionally, reset the flag to only restart components with changed configurations.
#. Choose Trigger Restart.

Use :ref:`Monitor Background Operations<ambari-monitor-backgroud-operations>` to monitor progress of rolling restarts.

.. Important::
  Rolling Restarts of DataNodes is recommended to only be performed during a cluster maintenance window.

**Setting Rolling Restart Parameters**

When you choose to restart slave components, use parameters to control how restarts of components roll. Parameter values based on ten percent of the total number of components in your cluster are set as default values. For example, default settings for a rolling restart of components in a 3-node cluster restarts one component at a time, waits two minutes between restarts, will proceed if only one failure occurs, and restarts all existing components that run this service.

If you trigger a rolling restart of components, Restart components with stale configs defaults to true. If you trigger a rolling restart of services, Restart services with stale configs defaults to false.

.. image:: /img/ambari/RlgRestart_DataNodes.png

Rolling restart parameter values must satisfy the following criteria:

+---------------------------+----------+---------------------------+---------------------------------------------------------------------+
| Parameter                 | Required | Value                     | Description                                                         |
+===========================+==========+===========================+=====================================================================+
| Batch Size                | Yes      | Must be an integer > = 0  | Number of components to include in each restart batch.              |
+---------------------------+----------+---------------------------+---------------------------------------------------------------------+
| Wait Time                 | Yes      | Must be an integer > = 0  | Time (in seconds) to wait between queuing each batch of components. |
+---------------------------+----------+---------------------------+---------------------------------------------------------------------+
| Tolerate up to x failures | Yes      | Must be an integer > = 0  | Total number of restart failures to tolerate, across all            |
|                           |          |                           | batches, before halting the restarts and not queuing batches.       |
+---------------------------+----------+---------------------------+---------------------------------------------------------------------+

**Aborting a Rolling Restart**

To abort future restart operations in the batch, choose Abort Rolling Restart.

.. image:: /img/ambari/abort_rllng_restart_option.png

.. _ambari-yarn-capacity-scheduler:

Refreshing YARN Capacity Scheduler
__________________________________

After you modify the Capacity Scheduler configuration, YARN supports refreshing the queues without requiring you to restart your ResourceManager. The “refresh” operation is valid if you have made no destructive changes to your configuration. Removing a queue is an example of a destructive change.

To refresh the Capacity Scheduler:

#. In Ambari Web, browse to ``Services > YARN > Summary``.
#. Select ``Service Actions``, then choose ``Refresh YARN Capacity Scheduler``.
#. Confirm you would like to perform this operation.

  The refresh operation is submitted to the YARN ResourceManager.

  .. Important::
    The Refresh operation will fail with the following message: “Failed to re-init queues” if you attempt to refresh queues in a case where you performed a destructive change, such as removing a queue. In cases where you have made destructive changes, you must perform a ResourceManager restart for the capacity scheduler change to take effect.

.. _ambari-rebalancing-hdfs:

Rebalancing HDFS
________________

HDFS provides a “balancer” utility to help balance the blocks across DataNodes in the cluster.

To initiate an HDFS rebalance from Ambari:

1. In Ambari Web, browse to ``Services > HDFS > Summary``.

2. Select ``Service Actions``, then choose ``Rebalance HDFS``.

3. Enter the Balance Threshold value as a percentage of disk capacity.

  .. image:: /img/ambari/RebalanceHDFS.png

4. Click ``Start`` to begin the rebalance.

5. You can check rebalance progress or cancel a rebalance in process by opening the Background Operations dialog.
