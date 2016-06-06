Optional: HTTP Cookie Persistence
=================================

During HTTP authentication, a cookie is dropped.
This is a persistent cookie that is valid across browser sessions.
For clusters that require enhanced security, it is desirable to have a session cookie that gets deleted when the user closes the browser session.

You can use the following property in the ``etc/hadoop/conf/core-site.xml`` file to specify cookie persistence across browser sessions.

::

  <property>
   <name>hadoop.http.authentication.cookie.persistent</name>
   <value>true</value>
  </property>

The default value for this property is ``false``.