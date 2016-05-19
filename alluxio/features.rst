*****************
Alluxio Features
*****************

==============
Tiered Storage
==============

Alluxio supports tiered storage, which allows to manage other storage types in addition to memory.
Currently, Alluxio Tiered Storage supports these storage types or tiers:

- MEM (Memory)
- SSD (Solid State Drives)
- HDD (Hard Disk Drives)

Using Alluxio with tiered storage allows Alluxio to store more data in the system at once,
since memory capacity may be limited in some deployments.
With tiered storage, Alluxio automatically manages blocks between all the configured tiers,
so users and administrators do not have to manually manage the locations of the data.

=================
Under File System
=================

Alluxio relies on some other storage system to safely persist the journal and user data.
This is the list of currently supported file systems:

- Local (Unix file system),
- HDFS,
- S3,
- Swift,
- GlusterFS.

Furthermore, it is easy to use any other file system extending the :code:`alluxio.underfs.UnderFileSystem` class.

|fdd| adopt HDFS as the default Alluxio |uss|.

When user creates files in the Alluxio storage, she can choose whether these objects should be persisted in the |ufs| storage or not.
Similarly, when a file is read from the |uss|, user can choose to promote it to Alluxio storage or not.
Those policies are called Write Type and Read Type.

====================
Write and Read Types
====================

Write Types
-----------

- `MUST_CACHE`: Write the file to Alluxio storage or failing the operation.
- `CACHE THROUGH`: Write the file synchronously to the |ufs|, and also try to write Alluxio storage.
- `THROUGH`: Write the file synchronously to the |uss|, skipping Alluxio storage.
- `ASYNC_THROUGH`: Write the file asynchronously to the |ufs|.

Read Types
----------

- `NO_CACHE`: Read the file and skip Alluxio storage. This read type will not cause any data migration or eviction in Alluxio storage.
- `CACHE`: Read the file and cache it in the highest tier of a local worker. This read type will not move data between tiers of Alluxio Storage. Users should use CACHE_PROMOTE for more optimized performance with tiered storage.
- `CACHE_PROMOTE`: Read the file and cache it in a local worker. Additionally, if the file was in Alluxio storage, it will be promoted to the top storage layer.

===================================
Unified and transparenting naming
===================================

Transparent naming maintains an identity between the Alluxio namespace and the |ufs| namespace.
When a user creates objects in the Alluxio namespace, they can choose whether these objects should be persisted in the |uss|. For objects that are persisted, Alluxio preserve the object paths, relative to the |uss| directory in which Alluxio objects are stored.

For instance, if a user creates a top-level directory named Users with subdirectories A and B, the directory structure and naming is preserved in the |ufs|. Similarly, when a user renames or deletes a persisted object in the Alluxio namespace, it is renamed or deleted in the |uss|.

Furthermore, Alluxio transparently discovers content present in the |uss| which was not created through Alluxio. For instance, if the |uss| contains a directory Data with files Reports and Sales, all of which were not created through Alluxio, their metadata will be loaded into Alluxio the first time they are accessed (e.g. when the user asks to list the contents of the top-level directory or when they request to open a file). The data of file is not loaded to Alluxio during this process.
