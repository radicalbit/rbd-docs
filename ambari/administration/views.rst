Managing Views
==============

The Ambari Views Framework offers a systematic way to plug in UI capabilities to surface custom visualization, management and monitoring features in Ambari Web. The development and use of Views allows you to extend and customize Ambari Web to meet your specific needs.

A View extends Ambari to let third parties plug in new resource types along with APIs, providers, and UIs to support them. A View is deployed into the Ambari Server and Ambari Admins can create View instances and set the privileges on access to users and groups.

The following sections cover the basics of Views and how to deploy and manage View instances in Ambari:

* :ref:`Terminology<ambari-view-terminology>`
* :ref:`Basic Concepts<ambari-view-basic-concepts>`
* :ref:`Deploying Views<ambari-view-deploy>`
* :ref:`Creating View Instances<ambari-view-create-instances>`
* :ref:`Setting View Permissions<ambari-setting-view-permissions>`

.. _ambari-view-terminology:

Terminology
___________

The following are Views terms and concepts you should be familiar with:

+--------------------+----------------------------------------------------------+
| Term               | Description                                              |
+====================+==========================================================+
| Views Framework    | The core framework that is used to develop a View. This  |
|                    | is very similar to a Java Web App.                       |
+--------------------+----------------------------------------------------------+
| View Definition    | Describes the View resources and core View properties    |
|                    | such as name, version and any necessary configuration    |
|                    | properties. On deployment, the View definition is read   |
|                    | by Ambari.                                               |
+--------------------+----------------------------------------------------------+
| View Package       | Packages the View client and server assets               |
|                    | (and dependencies) into a bundle that is ready to deploy |
|                    | into Ambari.                                             |
+--------------------+----------------------------------------------------------+
| View Deployment    | Deploying a View into Ambari. This makes the View        |
|                    | available to Ambari Admins for creating instances.       |
+--------------------+----------------------------------------------------------+
| View Name          | Unique identifier for a View. A View can have one or     |
|                    | more versions of a View. The name is defined in the View |
|                    | Definition (created by the View Developer) that is built |
|                    | into the View Package.                                   |
+--------------------+----------------------------------------------------------+
| View Version       | Specific version of a View. Multiple versions of a View  |
|                    | (uniquely identified by View name) can be deployed into  |
|                    | Ambari.                                                  |
+--------------------+----------------------------------------------------------+
| View Instance      | Instantiation of a specific View version. Instances are  |
|                    | created and configured by Ambari Admins and must have a  |
|                    | unique View instance name.                               |
+--------------------+----------------------------------------------------------+
| View Instance Name | Unique identifier of a specific instance of View.        |
+--------------------+----------------------------------------------------------+
| Framework Services | View context, instance data, configuration properties    |
|                    | and events are available from the Views Framework.       |
+--------------------+----------------------------------------------------------+

.. _ambari-view-basic-concepts:

Basic Concepts
______________

Views are basically Web applications that can be “plugged into” Ambari. Just like a typical web application, a View can include server-side resources and client-side assets. Server-side resources, which are written in Java, can integrate with external systems (such as cluster services) and expose REST end-points that are used by the view. Client-side assets, such as HTML/JavaScript/CSS, provide the UI for the view that is rendered in the Ambari Web interface.

Ambari Views Framework Ambari exposes the Views Framework as the basis for View development. The Framework provides the following:

* Method for describing and packaging a View
* Method for deploying a View
* Framework services for a View to integrate with Ambari
* Method for managing View versions, instances, and permissions

The Views Framework is separate from Views themselves. The Framework is a core feature of Ambari and Views build on that Framework. Although Ambari does include some Views out-of-the-box, the feature of Ambari is the Framework to enable the development, deployment and creation of views.

The development and delivery of a View follows this process flow:

* Develop the View (similar to how you would build a Web application)
* Package the View (similar to a WAR)
* Deploy the View into Ambari (using the Ambari Administration interface)
* Create and configure instances of the View (performed by Ambari Admins)

**Ambari Views Versions and Instances**

After Views are developed, views are identified by unique a view name. Each View can have one or more View versions. Each View name + version combination is deployed as a single View package. Once a View package is deployed, the Ambari Admin can create View instances, where each instance is identified by a unique View instance name. The Ambari Admin can then set access permissions for each View instance.

.. _ambari-view-deploy:

**Deploying a View**

Deploying a View involves obtaining the View Package and making the View available to the Ambari Server. Each View deployed has a unique name. Multiple versions of a View can be deployed at the same time. You can configure multiple versions of a View for your users, depending on their roles, and deploy these versions at the same time.

1. Obtain the View package. For example, ``files-0.1.0.jar``.

2. On the Ambari Server host, browse to the views directory.

  ::

    cd /var/lib/ambari-server/resources/views

3. Copy the View package into place.

4. Restart Ambari Server.

  ::

    ambari-server restart

5. The View is extracted, registered with Ambari, and displays in the Ambari Administration interface as available to create instances.

.. Note::
  ``/var/lib/ambari-server/resources/views`` is the default directory into which Views are deployed. You can change the default location by editing the ``views.dir`` property in ``ambari.properties``.

.. _ambari-view-create-instances:

Creating View Instances
_______________________

To create a View instance:

#. Browse to a View and expand.
#. Click the “Create Instance” button.
#. Provide the following information:

+-----------------------+----------+---------------------------------------------------------------------------+
| Item                  | Required | Description                                                               |
+=======================+==========+===========================================================================+
| View Version          | Yes      | Select the version of the View to instantiate.                            |
+-----------------------+----------+---------------------------------------------------------------------------+
| Instance Name         | Yes      | Must be unique for a given View.                                          |
+-----------------------+----------+---------------------------------------------------------------------------+
| Display Label         | Yes      | Readable display name used for the View instance when shown in Ambari Web.|
+-----------------------+----------+---------------------------------------------------------------------------+
| Description           | Yes      | Readable description used for the View instance when shown in Ambari Web. |
+-----------------------+----------+---------------------------------------------------------------------------+
| Visible               | No       | Designates whether the View is visible or not visible to the end-user in  |
|                       |          | Ambari web. Use this property to temporarily hide a view in Ambari Web    |
|                       |          | from users.                                                               |
+-----------------------+----------+---------------------------------------------------------------------------+
| Settings              | Maybe    | Depends on the View. If the View has a certain set of Settings that can   |
|                       |          | be customized, they will appear in this section. If a Setting is required,|
|                       |          | you are prompted to provide the required information.                     |
+-----------------------+----------+---------------------------------------------------------------------------+
| Cluster Configuration | Maybe    | Depends on the View. If the View has a set of Configuration properties    |
|                       |          | that can be derived from a cluster configuration, they will appear in     |
|                       |          | this section. If Ambari has a cluster configured that will work with the  |
|                       |          | View instance, then the choice of “Local Ambari Managed Cluster” will be  |
|                       |          | available (in lieu of having to enter the configuration manually).        |
+-----------------------+----------+---------------------------------------------------------------------------+


.. _ambari-setting-view-permissions:

Setting View Permissions
________________________

After a view instance has been created, an Ambari Admin can set which users and groups can access the view by setting the Use permission. By default, after view instance creation, no permissions are set on a view.

To set permissions on a view:

#. Browse to a view and expand. For example, browse to the Slider or Jobs view.
#. Click on the view instance you want to modify.
#. In the Permissions section, click the Users or Groups control.
#. Modify the user and group lists as appropriate.
#. Click the check mark to save changes.

.. Note::
  The Framework provides a way for view developers to specify custom permissions, beyond just the default Use permission. If custom permissions are are specified, they will show up in the Ambari Administration interface and the Ambari Admin can set users and groups on these permissions.