=====================================================
Installing, Configuring, and Deploying an RBD Cluster
=====================================================

Use the Ambari Install Wizard running in your browser to install, configure, and deploy your cluster, as follows:

Log In to Apache Ambari
_______________________

After starting the Ambari service, open Ambari Web using a web browser.

#. Point your browser to ``http://<your.ambari.server>:8080``, where ``<your.ambari.server>`` is the name of your ambari server host.
#. Log in to the Ambari Server using the default user name/password: ``admin/admin``. You can change these credentials later.

Launching the Ambari Install Wizard
___________________________________

From the Ambari Welcome page, choose Launch Install Wizard.

Name Your Cluster
_________________

#. In ``Name your cluster``, type a name for the cluster you want to create. Use no white spaces or special characters in the name.
#. Choose ``Next``.

Select Stack
____________

The Service Stack (the Stack) is a coordinated and tested set of |rbd-stack| components. Use a radio button to select the Stack version you want to install.
Expand Advanced Repository Options to select the Base URL of a repository from which Stack software packages download.

.. Note::
  The UI displays repository Base URLs based on Operating System Family (OS Family). Be sure to set the correct OS Family based on the Operating System you are running. The following table maps the OS Family to the Operating Systems.

**Operating Systems mapped to each OS Family**

+-----------+---------------------+
| OS Family | Operating Systems   |
+===========+=====================+
| redhat7   | Red Hat 7, CentOS 7 |
+-----------+---------------------+
| redhat6   | Red Hat 6, CentOS 6 |
+-----------+---------------------+

Install Options
_______________

In order to build up the cluster, the install wizard prompts you for general information about how you want to set it up. You need to supply the FQDN of each of your hosts. The wizard also needs to access the private key file you created in :doc:`Set Up Password-less SSH<../getting-ready/prepare-environment/ssh>`. Using the host names and key file information, the wizard can locate, access, and interact securely with all hosts in the cluster.

#. Use the ``Target Hosts`` text box to enter your list of host names, one per line. You can use ranges inside brackets to indicate larger sets of hosts. For example, for host01.domain through host10.domain use ``host[01-10].domain``
#. If you want to let Ambari automatically install the Ambari Agent on all your hosts using SSH, select ``Provide your SSH Private Key`` and either use the ``Choose File`` button in the ``Host Registration Information`` section to find the private key file that matches the public key you installed earlier on all your hosts or cut and paste the key into the text box manually.

  .. Note::
    If you are using IE 9, the ``Choose File`` button may not appear. Use the text box to cut and paste your private key manually.

    Fill in the user name for the SSH key you have selected. If you do not want to use root , you must provide the user name for an account that can execute sudo without entering a password.

#. If you do not want Ambari to automatically install the Ambari Agents, select ``Perform manual registration``. For further information, see :doc:`Installing Ambari Agents Manually</ambari/reference/install-agent>`.
#. Choose ``Register`` and ``Confirm`` to continue.

Confirm Hosts
_____________

``Confirm Hosts`` prompts you to confirm that Ambari has located the correct hosts for your cluster and to check those hosts to make sure they have the correct directories, packages, and processes required to continue the install.

If any hosts were selected in error, you can remove them by selecting the appropriate checkboxes and clicking the grey ``Remove Selected`` button. To remove a single host, click the small white **Remove** button in the Action column.

At the bottom of the screen, you may notice a yellow box that indicates some warnings were encountered during the check process. For example, your host may have already had a copy of ``wget`` or ``curl``. Choose ``Click here to see the warnings`` to see a list of what was checked and what caused the warning. The warnings page also provides access to a python script that can help you clear any issues you may encounter and let you run ``Rerun Checks``.

When you are satisfied with the list of hosts, choose ``Next``.


Choose Services
_______________

Based on the Stack chosen during Select Stack, you are presented with the choice of Services to install into the cluster. |rbd-stack| Stack comprises many services. You may choose to install any other available services now, or to add services later. The install wizard selects all available services for installation by default.

#. Choose ``none`` to clear all selections, or choose ``all`` to select all listed services.
#. Choose or clear individual checkboxes to define a set of services to install now.
#. After selecting the services to install now, choose ``Next``.

Assign Masters
______________

The Ambari install wizard assigns the master components for selected services to appropriate hosts in your cluster and displays the assignments in Assign Masters. The left column shows services and current hosts. The right column shows current master component assignments by host, indicating the number of CPU cores and amount of RAM installed on each host.

#. To change the host assignment for a service, select a host name from the drop-down menu for that service.
#. To remove a ZooKeeper instance, click the green minus icon next to the host address you want to remove.
#. When you are satisfied with the assignments, choose ``Next``.

Assign Slaves and Clients
_________________________

The Ambari installation wizard assigns the slave components (DataNodes, NodeManagers) to appropriate hosts in your cluster. It also attempts to select hosts for installing the appropriate set of clients.

#. Use ``all`` or ``none`` to select all of the hosts in the column or none of the hosts, respectively. If a host has an asterisk next to it, that host is also running one or more master components. Hover your mouse over the asterisk to see which master components are on that host.
#. Fine-tune your selections by using the checkboxes next to specific hosts.
#. When you are satisfied with your assignments, choose ``Next``.

Customize Services
__________________

The Customize Services step presents you with a set of tabs that let you review and modify your |rbd-stack| cluster setup. The wizard attempts to set reasonable defaults for each of the options. You are **strongly encouraged** to review these settings as your requirements might be slightly different.

Browse through each service tab and by hovering your cursor over each of the properties, you can see a brief description of what the property does. The number of service tabs shown depends on the services you decided to install in your cluster. **Any tab that requires input shows a red badge with the number of properties that need attention**. Select each service tab that displays a red badge number and enter the appropriate information.

**Directories**

The choice of directories where |rbd-stack| will store information is critical. Ambari will attempt to choose reasonable defaults based on the mount points available in your environment but you are **strongly encouraged** to review the default directory settings recommended by Ambari. In particular, confirm directories such as ``/tmp`` and ``/var`` are not being used for HDFS NameNode directories and DataNode directories under the **HDFS** tab.

**Service Account Users and Group**

The service account users and groups are available under the **Misc** tab. These are the **operating system accounts the service components will run as**. If these users do not exist on your hosts, Ambari will automatically create the users and groups locally on the hosts. If these users already exist, Ambari will use those accounts.

Depending on how your environment is configured, you might not allow groupmod or usermod operations. If this is the case, you **must** be sure all users and groups are already created and **be sure to** select the "Skip group modifications" option on the **Misc** tab. This tells Ambari to not modify group membership for the service users.

Refer to the :doc:`Ambari Reference Guide Customizing RBD Services</ambari/reference/customize-services>` for more information on the service account users and groups that are needed for |rbd-stack|.

After you complete Customizing Services, choose ``Next``.


Review
______

The assignments you have made are displayed. Check to make sure everything is correct. If you need to make changes, use the left navigation bar to return to the appropriate screen.

To print your information for later reference, choose ``Print``.

When you are satisfied with your choices, choose ``Deploy``.

Install, Start and Test
_______________________

The progress of the install displays on the screen. Ambari installs, starts, and runs a simple test on each component. Overall status of the process displays in progress bar at the top of the screen and host-by-host status displays in the main section. Do not refresh your browser during this process. Refreshing the browser may interrupt the progress indicators.

To see specific information on what tasks have been completed per host, click the link in the ``Message`` column for the appropriate host. In the ``Tasks`` pop-up, click the individual task to see the related log files. You can select filter conditions by using the ``Show`` drop-down list. To see a larger version of the log contents, click the ``Open`` icon or to copy the contents to the clipboard, use the ``Copy`` icon.

When ``Successfully installed and started the services`` appears, choose ``Next``.

Complete
________

The Summary page provides you a summary list of the accomplished tasks. Choose ``Complete``. Ambari Web GUI displays.