Optional: Ambari Web Inactivity Timeout
=======================================

Ambari is capable of automatically logging a user out of Ambari Web after a period of inactivity.
After a configurable amount of time, the user’s session will be terminated and they will be redirected to the login page.

This capability can be separately configured for Operators and Read-Only users.
This allows you to distinguish a read-only user (useful when Ambari Web is used as a monitoring dashboard) from other operators.
Alternatively, you can set both inactivity timeout values to be the same so that regardless of the user type, automatic logout will occur after a set period of time.

By default, the Ambari Web inactivity timeout is not enabled (i.e. is set to 0). The following instructions should be used to enable inactivity timeout and set as the amount of time in seconds before users are automatically logged out.

Ensure the Ambari Server is completely stopped before making changes to the inactivity timeout. Either make these changes before you start Ambari Server the first time, or bring the server down before making these changes.

1. On the Ambari Server host, open ``/etc/ambari-server/conf/ambari.properties`` with a text editor.

2. There are two properties for the inactivity timeout setting. Both are initially set to 0 (which means this capability is disabled).

  +---------------------------------------+--------------------------------------------------------------------------------+
  | Property                              | Description                                                                    |
  +=======================================+================================================================================+
  | user.inactivity.timeout.default       | Sets the inactivity timeout (in seconds) for all users except Read-Only users. |
  +---------------------------------------+--------------------------------------------------------------------------------+
  | user.inactivity.timeout.role.readonly | Sets the inactivity timeout (in seconds) for all Read-Only users.              |
  +---------------------------------------+--------------------------------------------------------------------------------+

3. Modify the values to enable the capability. The values are in seconds.

4. Save changes and restart Ambari Server.

5. After a user logs into Ambari Web, once a period of inactivity occurs, the user will be presented with an Automatic Logout dialog 60 seconds from logout. The user can click to remain logged in or if no activity occurs, Ambari Web will automatically log the user out and redirect the application to the login page.