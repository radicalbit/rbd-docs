|rbd-stack| and Kerberos Principals
===================================

Each service and sub-service in |rbd-stack| must have its own principal.
A **principal** name in a given realm consists of a primary name and an instance name, in this case the instance name is the FQDN of the host that runs that service.
As services do not log in with a password to acquire their tickets, their principal's authentication credentials are stored in a **keytab** file, which is extracted from the Kerberos database and stored locally in a secured directory with the service principal on the service component host.

.. image:: /img/ambari/Principals_and_Keytabs.png

**Principal and Keytab Naming Conventions**

+------------+----------------------------------------------------+---------------------------------------------+
| Asset      | Convention                                         | Example                                     |
+============+====================================================+=============================================+
| Principals | ``$service_component_name/$FQDN@EXAMPLE.COM``      | ``nn/c6401.ambari.apache.org@EXAMPLE.COM``  |
+------------+----------------------------------------------------+---------------------------------------------+
| Keytabs    | ``$service_component_abbreviation.service.keytab`` | ``/etc/security/keytabs/nn.service.keytab`` |
+------------+----------------------------------------------------+---------------------------------------------+

.. Note::
  In addition to the |rbd-stack| **Service Principals**, Ambari itself also requires a set of **Ambari Principals** to perform service “smoke” checks and alert health checks.
  Keytab files for the Ambari, or headless, principals reside on each cluster host, just as keytab files for the service principals.

Notice in the preceding example the primary name for each service principal.
These primary names, such as nn for example, represent the NameNode.
Each primary name has appended to it the instance name, the FQDN of the host on which it runs.
This convention provides a unique principal name for services that run on multiple hosts, like DataNodes and NodeManagers.
Adding the host name serves to distinguish, for example, a request from DataNode A from a request from DataNode B.
This is important for the following reasons:

* Compromised Kerberos credentials for one DataNode do not automatically lead to compromised Kerberos credentials for all DataNodes.
* If multiple DataNodes have exactly the same principal and are simultaneously connecting to the NameNode, and if the Kerberos authenticator being sent happens to have same timestamps, then the authentication is rejected as a replay request.