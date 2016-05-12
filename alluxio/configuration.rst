**********************
Alluxio Configuration
**********************


|fdd| provide Alluxio with the following configurations

- UnderFS: HDFS is the default UnderFs 
- Write Type: CACHE_THROUGH
- Read Type: CACHE_PROMOTE

Below a list of all the available configurations.
See the `official documentation <http://www.alluxio.org/documentation/en/Configuration-Settings.html/>`_ for more details.


+--------------------------------------------------+--------------------------------------------------+-----------------------------------------+ 
| Property                                         | Description                                      | Value                                   | 
+==================================================+==================================================+=========================================+ 
| alluxio.worker.evictor.class                     | Alluxio Worker Evictor Class                     | alluxio.worker.block.evictor.LRUEvictor |
+--------------------------------------------------+--------------------------------------------------+-----------------------------------------+ 
| alluxio.worker.memory                            | Alluxio Worker Memory                            | 2GB                                     |
+--------------------------------------------------+--------------------------------------------------+-----------------------------------------+ 
| alluxio.worker.tieredstore.levels                | Alluxio Worker Tieredstore Levels                | 1                                       |
+--------------------------------------------------+--------------------------------------------------+-----------------------------------------+ 
| alluxio.worker.tieredstore.level0.alias          | Alluxio Worker Tieredstore Level0 Alias          | MEM                                     |
+--------------------------------------------------+--------------------------------------------------+-----------------------------------------+ 
| alluxio.worker.tieredstore.level0.dirs.path      | Alluxio Worker Tieredstore Level0 Dirs Path      | /mnt/ramdisk                            |
+--------------------------------------------------+--------------------------------------------------+-----------------------------------------+ 
| alluxio.worker.tieredstore.level0.dirs.quota     | Alluxio Worker Tieredstore Level0 Dirs Quota     | 2GB                                     |
+--------------------------------------------------+--------------------------------------------------+-----------------------------------------+ 
| alluxio.worker.tieredstore.level0.reserved.ratio | Alluxio Worker Tieredstore Level0 Reserved Ratio | 0.1                                     |
+--------------------------------------------------+--------------------------------------------------+-----------------------------------------+