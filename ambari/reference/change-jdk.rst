Change the JDK Version
======================

During your initial Ambari Server Setup, you selected the JDK to use or provided a path to a custom JDK already installed on your hosts.
After setting up your cluster, you may change the JDK version using the following procedure.
Supported JDK versions are 1.7 and 1.8.

To change the JDK version for an existing cluster:

1. Re-run Ambari Server Setup.

  ::

    ambari-server setup

2. At the prompt to change the JDK, Enter ``y``.

  ::

    Do you want to change Oracle JDK [y/n] (n)? y

3. At the prompt to choose a JDK, Enter 1 to change the JDK to v1.8.

  ::

    [1] - Oracle JDK 1.8
    [2] - Oracle JDK 1.7
    [3] - Custom JDK

4. If you choose ``Oracle JDK 1.8`` or ``Oracle JDK 1.7``, the JDK you choose downloads and installs automatically on the Ambari Server host. This option requires that you have an internet connection. You must install this JDK on all hosts in the cluster to this same path.

5. If you choose ``Custom JDK``, verify or add the custom JDK path on all hosts in the cluster. Use this option if you want to use OpenJDK or do not have an internet connection (and have pre-installed the JDK on all hosts).

6. After setup completes, you must restart each component for the new JDK to be used by the Hadoop services.

7. Using the Ambari Web UI, do the following tasks:

  * Restart each component
  * Restart each host
  * Restart all services

.. Important::
  You must also update your JCE security policy files on the Ambari Server and all hosts in the cluster to match the new JDK version.
  If you are running Kerberos and do not update the JCE to match the JDK, you will have issues starting services. 