============
Alluxio File System API
============

Alluxio provides access to data through a filesystem interface. 
Alluxio provides two different Filesystem APIs, a native Java API and a Hadoop compatible API.

An example of the Hadoop API can be found :ref:`here<alluxio-hadoop-interface>`.

The native Java API can be included in a Maven Project by adding the following artifact.

.. literalinclude:: /rbp-docs-code/snippets/include-alluxio.xml
    :language: xml

The `official documentation <http://www.alluxio.org/documentation/en/File-System-API.html#getting-a-filesystem-client/>`_ 
provides a complete set of usage examples.

Here is a further example of how it is possible to load files from different UnderFs.

.. literalinclude:: /rbp-docs-code/src/main/java/radicalbit/io/java/AlluxioAPIExamples.java 
    :language: java
    :caption: Java
    :name: alluxio-api-example

