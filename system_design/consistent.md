# Consistent Hashing

The most important aspect is how the data will be partitioned.

Data Partitioning: distributing data across servers, scalability and performance.

Data Replication: copies of data, availability and durability.

Useful for:

-   Systems scaling up or down based on usage
-   Dynamic adjustment of cache usage
-   Replicate data shard

Dynamo, Cassandra

## Data Partitioning

How do we know on which node particular data is stored?

How do we know where data is moved when adding / removing nodes?

How to minimize movement?

## Consistent Hashing

Only a small set of keys move when servers are added / removed.

Data is stored in a ring with predefined ranges, start of each range is a token, MD5 Hashing.

When node is added / removed, only the next node is affected, but leads to non-uniform data and load.

## Virtual Nodes

Single token assigned to each node is a manual and fixed division of the ranges, which can be problematic with adding / removing nodes, hotspots, and node rebuilding.

The hash range is divided into multiple randomly distributed and non-contiguous smaller ranges (Virtual Nodes).

-   When a new node is added, it receives V-Nodes from existing nodes to maintain balance.
-   When rebuild, many nodes participate.
-   V-Nodes make it easier to maintain a cluster with different machines, more powerful more V-Nodes.
-   Decrease hot spots.

## Consistent Hashing for Replication

Each data item is replicated to N nodes, replication factor.

Each key is assigned a coordinator node and stores locally then replicate to N - 1 successor nodes.

In an eventually consistent system, the replication is done asynchronously.
