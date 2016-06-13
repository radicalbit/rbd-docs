Managing Configurations
=======================

Use Ambari Web to manage your |rbd-stack| component configurations. Select any of the following topics:

* :ref:`Configuring Services<ambari-configure-services>`
* :ref:`Using Host Config Groups<ambari-use-host-config-groups>`
* :ref:`Customizing Log Settings<ambari-customize-log>`
* :ref:`Downloading Client Configs<ambari-download-client-config>`
* :ref:`Service Configuration Versions<ambari-config-versions>`

.. _ambari-configure-services:

Configuring Services
____________________

Select a service, then select ``Configs`` to view and update configuration properties for the selected service. For example, select Cassandra, then select Configs. Expand a config category to view configurable service properties.

**Updating Service Properties**

1. Expand a configuration category.

2. Edit values for one or more properties that have the Override option. Edited values, also called stale configs, show an Undo option.

3. Choose Save.

**Restarting Components**

After editing and saving a service configuration, Restart indicates components that you must restart.

Select the Components or Hosts links to view details about components or hosts requiring a restart.

Then, choose an option appearing in Restart. For example, options to restart HDFS components include:

.. image:: /img/ambari/restart_options.png

.. _ambari-use-host-config-groups:

Using Host Config Groups
________________________

Ambari initially assigns all hosts in your cluster to one, default configuration group for each service you install. For example, after deploying a three-node cluster with default configuration settings, each host belongs to one configuration group that has default configuration settings for the HDFS service. In Configs, select ``Manage Config Groups``, to create new groups, re-assign hosts, and override default settings for host components you assign to each group.

.. image:: /img/ambari/manage_group.png

To create a Configuration Group:

1. Choose ``Add New Configuration Group``.

2. Name and describe the group, then choose Save.

3. Select a Config Group, then choose Add Hosts to Config Group.

4. Select Components and choose from available Hosts to add hosts to the new group.

  Select Configuration Group Hosts enforces host membership in each group, based on installed components for the selected service.

  .. image:: /img/ambari/SelectCnfgGrpHosts.png

5. Choose OK.

6. In Manage Configuration Groups, choose Save.

To edit settings for a configuration group:

1. In Configs, choose a Group.

2. Select a Config Group, then expand components to expose settings that allow Override.

3. Provide a non-default value, then choose Override or Save.

  Configuration groups enforce configuration properties that allow override, based on installed components for the selected service and group.

  .. image:: /img/ambari/EditCnfgGrpProperty.png

4. Override prompts you to choose one of the following options:

  .. image:: /img/ambari/override_config.png

  * Select an existing configuration group (to which the property value override provided in step 3 will apply), or
  * Create a new configuration group (which will include default properties, plus the property override provided in step 3).
  * hen, choose OK.

5. In Configs, choose Save.

.. _ambari-customize-log:

Customizing Log Settings
________________________

Ambari Web displays default logging properties in ``Service Configs > Custom log4j.properties``. Log 4j properties control logging activities for the selected service.

.. image:: /img/ambari/edit_log4jprops.png

.. _ambari-download-client-config:

Downloading Client Configs
__________________________

For Services that include client components (for example Hadoop Client), you can download the client configuration files associated with that client from Ambari.

#. In Ambari Web, browse to the Service with the client for which you want the configurations.
#. Choose ``Service Actions``.
#. Choose ``Download Client Configs``. You are prompted for a location to save the client configs bundle.
#. Save the bundle.

.. _ambari-config-versions:

Service Configuration Versions
______________________________

Ambari provides the ability to manage configurations associated with a Service. You can make changes to configurations, see a history of changes, compare + revert changes and push configuration changes to the cluster hosts.

**Basic Concepts**

It’s important to understand how service configurations are organized and stored in Ambari. Properties are grouped into Configuration Types (config types). A set of config types makes up the set of configurations for a service.

For example, the HDFS Service includes the following config types: hdfs-site, core-site, hdfs-log4j, hadoop-env, hadoop-policy. If you browse to ``Services > HDFS > Configs``, the configuration properties for these config types are available for edit.

Versioning of configurations is performed at the service-level. Therefore, when you modify a configuration property in a service, Ambari will create a Service Config Version. The figure below shows V1 and V2 of a Service Configuration Version with a change to a property in Config Type A. After making the property change to Config Type A in V1, V2 is created.

.. image:: /img/ambari/Svc_Cnfg_Vrsn_Cncpt.png

**Terminology**

The following table lists configuration versioning terms and concepts that you should know.

+----------------------------------+-------------------------------------------------------------------------------+
| Term                             | Description                                                                   |
+==================================+===============================================================================+
| Configuration Property           | Configuration property managed by Ambari, such as NameNode heapsize or        |
|                                  | replication factor.                                                           |
+----------------------------------+-------------------------------------------------------------------------------+
| Configuration Type (Config Type) | Group of configuration properties. For example: hdfs-site is a Config Type.   |
+----------------------------------+-------------------------------------------------------------------------------+
| Service Configurations           | Set of configuration types for a particular service. For example: hdfs-site   |
|                                  | and core-site Config Types are part of the HDFS Service Configuration.        |
+----------------------------------+-------------------------------------------------------------------------------+
| Change Notes                     | Optional notes to save with a service configuration change.                   |
+----------------------------------+-------------------------------------------------------------------------------+
| Service Config Version (SCV)     | Particular version of configurations for a specific service. Ambari saves a   |
|                                  | history of service configuration versions.                                    |
+----------------------------------+-------------------------------------------------------------------------------+
| Host Config Group (HCG)          | Set of configuration properties to apply to a specific set of hosts. Each     |
|                                  | service has a default Host Config Group, and custom config groups can be      |
|                                  | created on top of the default configuration group to target property overrides|
|                                  | to one or more hosts in the cluster. See Managing Configuration Groups for    |
|                                  | more information.                                                             |
+----------------------------------+-------------------------------------------------------------------------------+


**Saving a Change**

1. Make the configuration property change.

2. Choose Save.

3. You are prompted to enter notes that describe the change.

  .. image:: /img/ambari/Save_Config_Changes.png

4. Click Save to confirm your change. Cancel will not save but instead returns you to the configuration page to continuing editing. To revert the changes you made and not save, choose Discard. To return to the configuration page and continue editing without saving changes, choose Cancel.

**Viewing History**

Service Config Version history is available from Ambari Web in two places: On the Dashboard page under the Config History tab; and on each Service page under the Configs tab.

The ``Dashboard > Config History`` tab shows a list of all versions across services with each version number and the date and time the version was created. You can also see which user authored the change with the notes entered during save. Using this table, you can filter, sort and search across versions.

.. image:: /img/ambari/Cnfig_Hstry_1.png

The most recent configuration changes are shown on the ``Service > Configs`` tab. Users can navigate the version scrollbar left-right to see earlier versions. This provides a quick way to access the most recent changes to a service configuration.

.. image:: /img/ambari/Cnfig_Hstry_2.png

Click on any version in the scrollbar to view, and hover to display an option menu which allows you compare versions and perform a revert. Performing a revert makes any config version that you select the current version.

.. image:: /img/ambari/Cnfig_Hstry_3.png

**Comparing Versions**

When navigating the version scroll area on the ``Services > Configs`` tab, you can hover over a version to display options to view, compare or revert.

.. image:: /img/ambari/Cmpare_vrsns_1.png

To perform a compare between two service configuration versions:

#. Navigate to a specific configuration version. For example “V6”.
#. Using the version scrollbar, find the version would you like to compare against “V6”. For example, if you want to compare V6 to V2, find V2 in the scrollbar.
#. Hover over the version to display the option menu. Click “Compare”.
#. Ambari displays a comparison of V6 to V2, with an option to revert to V2.
#. Ambari also filters the display by only “Changed properties”. This option is available under the Filter control.

.. image:: /img/ambari/Cmpare_vrsns_2.png

**Reverting a Change**

You can revert to an older service configuration version by using the “Make Current” feature. The “Make Current” will actually create a new service configuration version with the configuration properties from the version you are reverting -- it is effectively a “clone”. After initiating the Make Current operation, you are prompted to enter notes for the new version (i.e. the clone) and save. The notes text will include text about the version being cloned.

.. image:: /img/ambari/revert_change_1.png

There are multiple methods to revert to a previous configuration version:

* View a specific version and click the “Make V* Current” button.

  .. image:: /img/ambari/revert_change_tabl_1.png

* Use the version navigation dropdown and click the “Make Current” button.

  .. image:: /img/ambari/revert_change_tabl_2.png

* Hover on a version in the version scrollbar and click the “Make Current” button.

  .. image:: /img/ambari/revert_change_tabl_3.png

* Perform a comparison and click the “Make V* Current” button.

  .. image:: /img/ambari/revert_change_tabl_4.png

**Versioning and Host Config Groups**

Service configuration versions are scoped to a host config group. For example, changes made in the default group can be compared and reverted in that config group. Same with custom config groups.

The following example describes a flow where you have multiple host config groups and create service configuration versions in each config group.

.. image:: /img/ambari/Svc_Config_Vrsn-01.png
.. image:: /img/ambari/Svc_Config_Vrsn-02.png
.. image:: /img/ambari/Svc_Config_Vrsn-03.png
.. image:: /img/ambari/Svc_Config_Vrsn-04.png
.. image:: /img/ambari/Svc_Config_Vrsn-05.png