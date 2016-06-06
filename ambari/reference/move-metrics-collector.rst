Moving the Ambari Metrics Collector
===================================

Use this procedure to move the Ambari Metrics Collector to a new host:

1. In Ambari Web , stop the Ambari Metrics service.

2. Execute the following API call to delete the current Metric Collector component.

  ::

    curl -u admin:admin -H "X-Requested-By:ambari" - i -X DELETE \
      http://ambari.server:8080/api/v1/clusters/cluster.name/hosts/metrics.collector.hostname/host_components/METRICS_COLLECTOR

  where ``ambari.server`` is the Ambari Server host, ``cluster.name`` is your Cluster Name, and ``metrics.collector.hostname`` is the host running the Metrics Collector.

3. Execute the following API call to add Metrics Collector to a new host.

  ::

    curl -u admin:admin -H "X-Requested-By:ambari" - i -X POST \
      http://ambari.server:8080/api/v1/clusters/cluster.name/hosts/metrics.collector.hostname/host_components/METRICS_COLLECTOR

  where ``ambari.server`` is the Ambari Server host, ``cluster.name`` is your Cluster Name, and ``metrics.collector.hostname`` is the host that will run the Metrics Collector.

4. In Ambari Web, go the Host page where you installed the new Metrics Collector. Click to Install the Metrics Collector component from the Host page.

5. In Ambari Web, start the Ambari Metrics service.

6. For every service, use ``Ambari Web > Service Actions > Restart All`` to start sending metrics to the new collector.