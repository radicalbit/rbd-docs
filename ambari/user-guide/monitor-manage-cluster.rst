Monitoring and Managing Your Cluster
====================================

This topic describes how to use Ambari Web features to monitor and manage your |rbd-stack| cluster.
To navigate, select one of the following feature tabs located at the top of the Ambari main window.

* :ref:`Viewing the Cluster Dashboard<ambari-view-cluster-dashboard>`
* :ref:`Modifying the Cluster Dashboard<ambari-modify-cluster-dashboard>`
* :ref:`Viewing Cluster Heatmaps<ambari-cluster-heatmaps>`

.. _ambari-view-cluster-dashboard:

Viewing the Cluster Dashboard
_____________________________

Ambari Web displays the Dashboard page as the home page. Use the Dashboard to view the operating status of your cluster.
Each metrics widget displays status information for a single service in your |rbd-stack| cluster.
The Dashboard displays all metrics for the HDFS service, and cluster-wide metrics by default.
You can add and remove individual widgets, and rearrange the Dashboard by dragging and dropping each widget to a new location in the dashboard.
Status information appears as simple pie and bar charts, more complex charts showing usage and load, sets of links to additional data sources, and values for operating parameters such as uptime and average RPC queue wait times.
Most widgets display a single fact by default.
For example, HDFS Disk Usage displays a load chart and a percentage figure.

.. image:: /img/ambari/Ambari_dashboard.png

.. Note::
  Each Service installed in your cluster also has a Service-specific dashboard. Refer to :ref:`Modifying the Service Dashboard<ambari-modify-service-dashboard>` section for more information.

**Scanning Service Status**

Notice the color of the dot appearing next to each component name in a list of components, services or hosts.
The dot color and blinking action indicates operating status of each component, service, or host.
For example, in the :ref:`Summary View<ambari-service-summary-alerts>`, notice green dot next to each service name.
The following colors and actions indicate service status:

+----------------+------------------------------+
| Color          | Status                       |
+================+==============================+
| Solid Green    | All masters are running      |
+----------------+------------------------------+
| Blinking Green | Starting up                  |
+----------------+------------------------------+
| Solid Red      | At least one master is down  |
+----------------+------------------------------+
| Blinking Red   | Stopping                     |
+----------------+------------------------------+

Click the service name to open the Services screen, where you can see more detailed information on each service.

**Widget Descriptions**

View Metrics that indicate the operating status of your cluster on the Ambari Dashboard.
Each metrics widget displays status information for a single service in your |rbd-stack| cluster.
The Ambari Dashboard displays all metrics for HDFS and cluster-wide metrics by default.

You can add and remove individual widgets, and rearrange the dashboard by dragging and dropping each widget to a new location in the dashboard.

Status information appears as simple pie and bar charts, more complex charts showing usage and load, sets of links to additional data sources, and values for operating parameters such as uptime and average RPC queue wait times.
Most widgets display a single fact by default.

**Widget Details**

To see more detailed information about a service, hover your cursor over a Metrics widget.

More detailed information about the service displays, as shown in the following example:

.. image:: /img/ambari/HDFS_widget_example.png

* To remove a widget from the mashup, click the white ``X``.
* To edit the display of information in a widget, click the pencil icon. For more information about editing a widget, see :ref:`Customizing Metrics Display<ambari-customize-widget-display>`.

**Linking to Service UIs**

The HDFS Links widget list |rbd-stack| components for which links to more metrics information, such as thread stacks, logs and native component UIs are available.
For example, you can link to NameNode, Secondary NameNode, and DataNode components for HDFS, using the links shown in the following example:

.. image:: /img/ambari/HDFS_widget_links.png

Choose the `More` drop-down to select from the list of links available for each service.

**Viewing Cluster-Wide Metrics**

Cluster-wide metrics display information that represents your whole cluster. The Ambari Dashboard shows the following cluster-wide metrics:

.. image:: /img/ambari/cluster_wide_metrics_2.png

Ambari Cluster-Wide Metrics and Descriptions:

+---------------+-------------------------------------------------------------------------------+
| Metric        | Description                                                                   |
+===============+===============================================================================+
| Memory Usage  | The cluster-wide memory utilization, including memory cached, swapped, used,  |
|               | shared.                                                                       |
+---------------+-------------------------------------------------------------------------------+
| Network Usage | The cluster-wide network utilization, including in-and-out.                   |
+---------------+-------------------------------------------------------------------------------+
| CPU Usage     | Cluster-wide CPU information, including system, user and wait IO.             |
+---------------+-------------------------------------------------------------------------------+
| Cluster Load  | Cluster-wide Load information, including total number of nodes. total number  |
|               | of CPUs, number of running processes and 1-min Load.                          |
+---------------+-------------------------------------------------------------------------------+

* To remove a widget from the dashboard, click the white ``X``.
* Hover your cursor over each cluster-wide metric to magnify the chart or itemize the widget display.
* To remove or add metric items from each cluster-wide metric widget, select the item on the widget legend.
* To see a larger view of the chart, select the magnifying glass icon.

Ambari displays a larger version of the widget in a pop-out window, as shown in the following example:

.. image:: /img/ambari/cluster_wide_metrics_detail.png

.. _ambari-modify-cluster-dashboard:

Use the pop-up window in the same ways that you use cluster-wide metric widgets on the dashboard.

To close the widget pop-up window, choose OK.

Modifying the Cluster Dashboard
_______________________________

You can customize the Ambari Dashboard in the following ways:

**Adding a Widget to the Dashboard**

To replace a widget that has been removed from the dashboard:

1. Select the Metrics drop-down, as shown in the following example:

  .. image:: /img/ambari/add_a_widget.png

2. Choose Add.
3. Select a metric, such as Region in Transition.
4. Choose Apply.


**Resetting the Dashboard**

To reset all widgets on the dashboard to display default settings:

1. Select the Metrics drop-down, as shown in the following example:

  .. image:: /img/ambari/edit_widget_dashboard.png

2. Choose Edit.
3. Choose Reset all widgets to default.

.. _ambari-customize-widget-display:

**Customizing Widget Display**

To customize the way a service widget displays metrics information:

1. Hover your cursor over a service widget.
2. Select the pencil-shaped, edit icon that appears in the upper-right corner.

  The Customize Widget pop-up window displays properties that you can edit, as shown in the following example.

  .. image:: /img/ambari/customize_widget.png

3. Follow the instructions in the Customize Widget pop-up to customize widget appearance.
4. To save your changes and close the editor, choose Apply.
5. To close the editor without saving any changes, choose Cancel.

.. Note::
  Not all widgets support editing.

.. _ambari-cluster-heatmaps:

Viewing Cluster Heatmaps
________________________

Heatmaps provides a graphical representation of your overall cluster utilization using simple color coding.

.. image:: /img/ambari/cluster_heatmaps.png

A colored block represents each host in your cluster. To see more information about a specific host, hover over the block representing the host in which you are interested.
A pop-up window displays metrics about |rbd-stack| components installed on that host.
Colors displayed in the block represent usage in a unit appropriate for the selected set of metrics.
If any data necessary to determine state is not available, the block displays "Invalid Data".
Changing the default maximum values for the heatmap lets you fine tune the representation.
Use the Select Metric drop-down to select the metric type.

.. image:: /img/ambari/cluster_heatmaps_select_metrics.png

Heatmaps supports the following metrics:

+------------------------------+----------------------------------------+
| Metric                       | Uses                                   |
+==============================+========================================+
| Host/Disk Space Used %       | disk.disk_free and disk.disk_total     |
+------------------------------+----------------------------------------+
| Host/Memory Used %           | memory.mem_free and / memory.mem_total |
+------------------------------+----------------------------------------+
| Host/CPU Wait I/O %          | cpu.cpu_wio                            |
+------------------------------+----------------------------------------+
| HDFS/Bytes Read              | dfs.datanode.bytes_read                |
+------------------------------+----------------------------------------+
| HDFS/Bytes Written           | dfs.datanode.bytes_written             |
+------------------------------+----------------------------------------+
| HDFS/Garbage Collection Time | jvm.gcTimeMillis                       |
+------------------------------+----------------------------------------+
| HDFS/JVM Heap MemoryUsed     | jvm.memHeapUsedM                       |
+------------------------------+----------------------------------------+