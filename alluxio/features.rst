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

=======
Lineage
=======

Alluxio can achieve high throughput writes and reads, without compromising fault-tolerance by using Lineage, where lost output is recovered by re-executing the jobs that created the output.
With lineage, applications write output into memory, and Alluxio periodically checkpoints the output into the under file system in an asynchronous fashion. In case of failures, Alluxio launches job recomputation to restore the lost files. Lineage assumes that jobs are deterministic so that the recomputed outputs are identical. If this assumption is not met, it is up to the application to handle divergent outputs.
By default, lineage is not enabled. It can be enabled by setting the Alluxio.user.lineage.enabled property to true in the configuration file.

===================================
Unified and transparenting naming
===================================

Transparent naming maintains an identity between the Alluxio namespace and the underfs namespace.
When a user creates objects in the Alluxio namespace, they can choose whether these objects should be persisted in the underlying storage system. For objects that are persisted, Alluxio preserve the object paths, relative to the underlying storage system directory in which Alluxio objects are stored. For instance, if a user creates a top-level directory Users with subdirectories A and B, the directory structure and naming is preserved in the underfs. Similarly, when a user renames or deletes a persisted object in the Alluxio namespace, it is renamed or deleted in the underlying storage system.
Furthermore, Alluxio transparently discovers content present in the underlying storage system which was not created through Alluxio. For instance, if the underlying storage system contains a directory Data with files Reports and Sales, all of which were not created through Alluxio, their metadata will be loaded into Alluxio the first time they are accessed (e.g. when the user asks to list the contents of the top-level directory or when they request to open a file). The data of file is not loaded to Alluxio during this process.