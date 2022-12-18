# System Design

## Glossary
-   [Key Characteristics](./characteristics.md)
-   [Load Balancing](./load_balancing.md)
-   [Caching](./caching.md)
-   [Data Partitioning](./partition.md)
-   [Indexes](./indexes.md)
-   [Proxies](./proxies.md)
-   [Redundancy and Replication](./redundancy.md)
-   [SQL v.s. NoSQL](./sql.md)
-   [CAP](./cap.md)
-   [PACELC](./pacelc.md)
-   [Consistent Hashing](./consistent.md)
-   [Long Polling / Websockets / Server Sent](./polling.md)
-   [Blooming Filters](./blooming.md)
-   [Quorum](./quorum.md)
-   [Leader and Follower](./leader.md)
-   [Heartbeat](./heartbeat.md)
-   [Checksum](./checksum.md)
-   [Asynchronism](./async.md)
-   [Domain Name System](./dns.md)
-   [Content Delivery Network](./cdn.md)
-   [Application Layer](./application.md)
-   [Communication](./communication.md)
-   [Stateless](./stateless.md)
-   [Data Center](./center.md)
-   [Message Queue](./message.md)
-   [Logging / Metrics / Automation](./logging.md)
-   [Back of the Envelope Estimation](./estimation.md)

## Case Studies
-   [Step by Step](./guide.md)

## Scaling to Millions
-   Stateless web tier
-   Redundancy at every tier
-   Cache data
-   Multiple data centers
-   CDN
-   Scale data tier by sharding
-   Split tiers into individual services
-   Monitor and automate

## Trade-offs
-   [Trade Offs](./trade.md)

## Real World
-   Data processing
    -   [MapReduce (Google)](https://research.google.com/archive/mapreduce-osdi04.pdf)
    -   Spark (Databricks)
    -   Storm (Twitter)

-   Data store
    -   [BigTable (column-oriented, Google)](https://research.google.com/archive/bigtable-osdi06.pdf)
    -   HBase (open source BigTable)
    -   [Cassandra (column-oriented, Facebook)](http://www.cl.cam.ac.uk/~ey204/teaching/ACS/R212_2014_2015/papers/lakshman_ladis_2009.pdf)
    -   [DynamoDB (document-oriented, Amazon)](https://www.amazon.science/publications/dynamo-amazons-highly-available-key-value-store)
    -   MongoDB (column-oriented)
    -   Spanner (global, Google)
    -   Memcached (cache)
    -   Redis (cache)

-   File system
    -   [Google file system, GFS](https://research.google/pubs/pub51/)
    -   HDFS (open source GFS)

-   Kafka (message queue, Linkedin)

## Object Storage

https://www.netapp.com/data-storage/storagegrid/what-is-object-storage/

https://en.wikipedia.org/wiki/Object_storage

## Caches
https://en.wikipedia.org/wiki/Memcached

https://en.wikipedia.org/wiki/Redis
