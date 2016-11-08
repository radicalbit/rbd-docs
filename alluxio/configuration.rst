**********************
Alluxio Configuration
**********************


|fdd| provides Alluxio with HDFS as the default |ufs|

The table below shows a list of all the available configurations.
See the `official documentation <http://www.alluxio.org/docs/1.2/en/Configuration-Settings.html>`_ for more details.


+----------------------------------------------------+----------------------------------------------------+--------------------------------------------------------------+
| | Property                                         | | Description                                      | | Value                                                      |
+====================================================+====================================================+==============================================================+
| | alluxio.user.file.readtype.default               | | Default read type when creating Alluxio files    | | CACHE_PROMOTE                                              |
|                                                    |                                                    | | (move data to highest tier if already in Alluxio storage,  |
|                                                    |                                                    | | write data into highest tier of local Alluxio              |
|                                                    |                                                    | | if data needs to be read from under storage)               |
+----------------------------------------------------+----------------------------------------------------+--------------------------------------------------------------+
| | alluxio.user.file.writetype.default              | | Default write type when creating Alluxio files.  | | CACHE_THROUGH                                              |
|                                                    |                                                    | | (try to cache, write to UnderFS synchronously)             | 
+----------------------------------------------------+----------------------------------------------------+--------------------------------------------------------------+
| | alluxio.worker.evictor.class                     | | Alluxio Worker Evictor Class                     | | alluxio.worker.block.evictor.LRUEvictor                    |
+----------------------------------------------------+----------------------------------------------------+--------------------------------------------------------------+
| | alluxio.worker.memory                            | | Alluxio Worker Memory                            | | 2GB                                                        |
+----------------------------------------------------+----------------------------------------------------+--------------------------------------------------------------+
| | alluxio.worker.tieredstore.levels                | | Alluxio Worker Tieredstore Levels                | | 1                                                          |
+----------------------------------------------------+----------------------------------------------------+--------------------------------------------------------------+
| | alluxio.worker.tieredstore.level0.alias          | | Alluxio Worker Tieredstore Level0 Alias          | | MEM                                                        |
+----------------------------------------------------+----------------------------------------------------+--------------------------------------------------------------+
| | alluxio.worker.tieredstore.level0.dirs.path      | | Alluxio Worker Tieredstore Level0 Dirs Path      | | /mnt/ramdisk                                               |
+----------------------------------------------------+----------------------------------------------------+--------------------------------------------------------------+
| | alluxio.worker.tieredstore.level0.dirs.quota     | | Alluxio Worker Tieredstore Level0 Dirs Quota     | | 2GB                                                        |
+----------------------------------------------------+----------------------------------------------------+--------------------------------------------------------------+
| | alluxio.worker.tieredstore.level0.reserved.ratio | | Alluxio Worker Tieredstore Level0 Reserved Ratio | | 0.1                                                        |
+----------------------------------------------------+----------------------------------------------------+--------------------------------------------------------------+
