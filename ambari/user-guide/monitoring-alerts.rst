Monitoring and Alerts
=====================

Ambari monitors cluster health and can alert you in the case of certain situations to help you identify and troubleshoot problems.
You manage how alerts are organized, under which conditions notifications are sent, and by which method.
This section provides information on:

* :ref:`Managing Alerts<ambari-managing-alerts>`
* :ref:`Configuring Notifications<ambari-config-notifications>`

.. _ambari-managing-alerts:

Managing Alerts
_______________

Ambari predefines a set of alerts that monitor the cluster components and hosts.
Each alert is defined by an Alert Definition, which specifies the Alert Type check interval and thresholds.
When a cluster is created or modified, Ambari reads the Alert Definitions and creates Alert Instances for the specific items to watch in the cluster.
For example, if your cluster includes HDFS, there is an alert definition to watch the "DataNode Process".
An instance of that alert definition is created for each DataNode in the cluster.

Using Ambari Web, you can browse the list of alerts defined for your cluster under the Alerts tab.
You can search and filter alert definitions by current status, by last status change and the service the alert definition is associated with among other things.
Click on the alert definition name to view the details about that alert, modify the alert properties (such as check interval and thresholds) and the list of alert instances associated with that alert definition.

Each alert instance reports an Alert Status defined by severity.
The most common severity levels are OK, WARNING, CRITICAL but there are also severities for UNKNOWN and NONE.
Alert notifications will be sent on alert status changes (for example, going from OK to CRITICAL).
See :ref:`Configuring Notifications<ambari-config-notifications>` for more information about notifications.

**Modifying an Alert**

General properties for an alert include Name, Description and Check Interval.
The Check Interval defines the frequency Ambari will check the alert status.
For example, a "1 minute" interval means Ambari checks the alert status every "1 minute".

The configuration options for thresholds depend on the Alert Type.

#. Browse to the Alerts section in Ambari Web.
#. Find the alert definition and click to view the definition details.
#. Click Edit to modify the name, description, check interval and thresholds (as applicable).
#. Click Save.
#. Changes will take effect on all alert instances at the next check interval.

**Enabling or Disabling Alerts**

You can optionally disable alerts. When an alert is disabled, no alert instances are in effect and Ambari will no longer perform the checks for the alert.
Therefore, no alert status changes will be recorded and no notifications (i.e. no emails or SNMP traps) will dispatched.

#. Browse to the Alerts section in Ambari Web.
#. Find the alert definition. Click the Enabled or Disabled text to enable/disable the alert.
#. Alternatively, you can click on the alert to view the definition details and click Enabled or Disabled to enable/disable the alert.
#. You will be prompted to confirm enable/disable.

**Alert Types**

Alert thresholds and the threshold units are dependent on alert type. The following table lists the types of alerts, their possible status and if the thresholds are configurable:

+------------+------------------------------------------------------------------+-------------------------+-----------------+
| Alert Type | Description                                                      | Thresholds Configurable | Threshold Units |
+============+==================================================================+=========================+=================+
| WEB        | Connects to a Web URL. Alert status is based on the HTTP         | No                      | n/a             |
|            | response code.                                                   |                         |                 |
+------------+------------------------------------------------------------------+-------------------------+-----------------+
| PORT       | Connects to a port. Alert status is based on response time.      | Yes                     | seconds         |
+------------+------------------------------------------------------------------+-------------------------+-----------------+
| METRIC     | Checks the value of a service metric. Units vary, based on the   | Yes                     | varies          |
|            | metric being checked.                                            |                         |                 |
+------------+------------------------------------------------------------------+-------------------------+-----------------+
| AGGREGATE  | Aggregates the status for another alert.                         | Yes                     | %               |
+------------+------------------------------------------------------------------+-------------------------+-----------------+
| SCRIPT     | Executes a script to handle the alert check.                     | No                      | n/a             |
+------------+------------------------------------------------------------------+-------------------------+-----------------+

**WEB Alert Type**

WEB alerts watch a Web URL on a given component and the alert status is determined based on the HTTP response code.
Therefore, you cannot change what HTTP response codes determine the thresholds for WEB alerts.
Although you can customize what the response text for each threshold.
The response code and corresponding status for WEB alerts:

* OK status if Web URL responds with code under 400.
* WARNING status if Web URL responds with code 400 and above.
* CRITICAL status if Ambari cannot connect to Web URL.

.. Note::
  The connection timeout defaults to 5.0 seconds on the connection_timeout property on the alert definition when accessed from the Alerts API.

  ::

    GET /api/v1/clusters/MyCluster/alert_definitions/42

     "source" : {
        "reporting" : {
          ...
        },
        "type" : "WEB",
        "uri" : {
          ...
          "connection_timeout" : 5.0
        }
      }

**PORT Alert Type**

PORT alerts check the response time to connect to a given a port and the threshold units are based on seconds.

**METRIC Alert Type**

METRIC alerts check the value of a single or multiple metrics (if a calculation is performed).
The metric is accessed from a URL endpoint available on a given component.
The thresholds are adjustable and the units for each threshold are metric-dependent.
For example, in the case of “CPU utilization” alerts, the unit is “%”.
And in the case of “RPC latency” alerts, the unit is “milliseconds (ms)”.

.. Note::
  The connection timeout defaults to 5.0 seconds on the connection_timeout property on the alert definition when accessed from the Alerts API

  ::

    GET /api/v1/clusters/MyCluster/alert_definitions/32

     "source" : {
        "reporting" : {
          ...
        },
        "type" : "METRIC",
        "uri" : {
          ...
          "connection_timeout" : 5.0
        }
      }

**AGGREGATE Alert Type**

AGGREGATE alerts aggregate the alert status as a percentage of the alert instances affected.
For example, the “Percent DataNode Process” alert aggregates the “DataNode Process” alert.
The threshold units are “%”.

**SCRIPT Alert Type**

SCRIPT alerts execute a script and the script determines status such as OK, WARNING or CRITICAL.
The thresholds and response text built-into the alert definitions but are not modifiable from the Ambari Web UI.

.. Note::
  The location of the script is available on the path property on the alert definition when accessed from the Alerts API.

  ::

    GET /api/v1/clusters/MyCluster/alert_definitions/19

     "source" : {
        "parameters" : {
          ...
        },
        "path" : "HDFS/2.7.1/package/alerts/alert_ha_namenode_health.py",
        "type" : "SCRIPT"
      }

.. _ambari-config-notifications:

Configuring Notifications
_________________________

With Alert Groups and Notifications, you can create groups of alerts and setup notification targets for each group.
This way, you can notify different parties interested in certain sets of alerts via different methods.
For example, you might want your |rbd-stack| Operations team to receive all alerts via EMAIL, regardless of status.
And at the same time, have your System Administration team receive all RPC and CPU related alerts that are Critical only via SNMP.
To achieve this scenario, you would have an Alert Notification that handles Email for all alert groups for all severity levels, and you would have a different Alert Notification group that handles SNMP on critical severity for an Alert Group that contains the RPC and CPU alerts.

Ambari defines a set of default Alert Groups for each service installed in the cluster.
For example, you will see a group for HDFS Default.
These groups cannot be deleted and the alerts in these groups are not modifiable.
If you choose not to use these groups, just do not set a notification target for them.

**Creating or Editing Notifications**

1. Browse to the Alerts section in Ambari Web.

2. Under the Actions menu, click Manage Notifications.

3. The list of existing notifications is shown.

4. Click + to “Create new Alert Notification”. The Create Alert Notification dialog is displayed.

5. Enter the notification name, select the groups to which the notification should be assigned (all or a specific set), select the Severity levels that this notification responds to, include a description, and choose the method for notification (EMAIL or SNMP).

  * For **EMAIL**: provide information about your SMTP infrastructure such as SMTP Server, Port, To/From address and if authentication is required to relay messages through the server. You can add custom properties to the SMTP configuration based on the `Javamail SMTP options <https://javamail.java.net/nonav/docs/api/com/sun/mail/smtp/package-summary.html>`_.

    +--------------------+-------------------------------------------------------------------------------------------+
    | Parameter          | Description                                                                               |
    +====================+===========================================================================================+
    | Email To           | A comma-separated list of one or more email addresses to send the alert email.            |
    +--------------------+-------------------------------------------------------------------------------------------+
    | SMTP Server        | The FQDN or IP address of the SMTP server to use to relay the alert email.                |
    +--------------------+-------------------------------------------------------------------------------------------+
    | SMTP Port          | The SMTP port on the SMTP Server.                                                         |
    +--------------------+-------------------------------------------------------------------------------------------+
    | Email From         | A single email address to be the “from” alert email.                                      |
    +--------------------+-------------------------------------------------------------------------------------------+
    | Use Authentication | Check if your SMTP Server requires authentication in order to relay messages. Be sure to  |
    |                    | also provide the username and password credentials.                                       |
    +--------------------+-------------------------------------------------------------------------------------------+

  * For **SNMP**: select the SNMP version, Community, Host, and Port where the SNMP trap should be sent. Also, the OID parameter must be configured properly for SNMP trap context. If no custom, or enterprise-specific OID will be used, we recommend the following:

    +--------------------+-------------------------------------------------------------------------------------------+
    | Parameter          | Description                                                                               |
    +====================+===========================================================================================+
    | OID                | 1.3.6.1.4.1.18060.16.1.1                                                                  |
    +--------------------+-------------------------------------------------------------------------------------------+
    | Hosts              | A comma-separated list of one or more Host FQDNs of where to send the trap.               |
    +--------------------+-------------------------------------------------------------------------------------------+
    | Port               | The port where snmptrapd is listening on the Hosts.                                       |
    +--------------------+-------------------------------------------------------------------------------------------+

    .. Note::
      Only SNMPv1 and SNMPv2c should be chosen for SNMP Version. SNMPv3 is not supported nor functional at this time.

6. After completing the notification, click Save.

**Creating or Editing Alert Groups**

#. Browse to the Alerts section in Ambari Web.
#. From the Actions menu, choose Manage Alert Groups
#. The list of existing groups (default and custom) is shown.
#. Choose + to “Create Alert Group”. Enter the Group a name and click Save.
#. By clicking on the custom group in the list, you can add or delete alert definitions from this group, and change the notification targets for the group.

**Dispatching Notifications**

When an alert is enabled and the alert status changes (for example, from OK to CRITICAL or CRITICAL to OK),
Ambari will send a notification (depending on how the user has configured notifications).

For **EMAIL** notifications: Ambari will send an email digest that includes all alert status changes.
For example: if two alerts go CRITICAL, Ambari sends one email that says "Alert A is CRITICAL and Ambari B alert is CRITICAL".
Ambari will not send another email notification until status has changed again.

For **SNMP** notifications: Ambari will fire an SNMP trap per alert status change.
For example: if two alerts go CRITICAL, Ambari will fire two SNMP traps, one for each alert going OK -> CRITICAL.
When the alert changes status from CRITICAL -> OK, another trap is sent.

**Viewing Alert Status Log**

In addition to dispatching alert notifications, Ambari writes alert status changes to a log on the Ambari Server host.
Alert status changes will be written to the log regardless if EMAIL or SNMP notifications are configured.

1. On the Ambari Server host, browse to the log directory:

  ::

    cd /var/log/ambari-server/

2. View the ambari-alerts.log file.

3. Log entries will include the time of the status change, the alert status, the alert definition name and the response text.

