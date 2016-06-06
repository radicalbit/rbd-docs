Setting up an Internet Proxy Server for Ambari
==============================================

If you plan to use the public repositories for installing the distribution, Ambari Server must have Internet access to confirm access to the repositories and validate the repositories.
If your machine requires use of a proxy server for Internet access, you must configure Ambari Server to use the proxy server.

To setup an internet proxy server for Ambari:

1. On the Ambari Server host, add proxy settings to the following script: ``/var/lib/ambari-server/ambari-env.sh``.

  ::

    -Dhttp.proxyHost=<yourProxyHost> -Dhttp.proxyPort=<yourProxyPort>

2. Optionally, to prevent some host names from accessing the proxy server, define the list of excluded hosts, as follows:

  ::

    -Dhttp.nonProxyHosts=<pipe|separated|list|of|hosts>

3. If your proxy server requires authentication, add the user name and password, as follows:

  ::

    -Dhttp.proxyUser=<username> -Dhttp.proxyPassword=<password>

4. Restart the Ambari Server to pick up this change.