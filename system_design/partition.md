# Data Partitioning

Splitting up a database/table to improve manageability, performance, availability and load balancing.

Scale horizonatally.

## Methods
-   Horizontal partitioning (Data sharding): range based partitioning. May lead to unbalanced servers.

-   Vertical partitioning: store tables related to specifc features. May be necesary to further partition.

-   Directory-Based Partitioning: directory server that holds the mapping between each tuple key to its database server.

## Criteria
-   Key or Hash-Based: uniform allocation. Number of database is fixed, when adding new servers hashing changes, workaround is [Consistent Hashing](./consistent.md).

-   List Partitioning: each partition is assigned a list of values. Lookup values in each partition.

-   Round Robin: 

-   Composite: 

## Problems

-   Joins and Denormalization: 

-   Referential Integrity: 

-   Rebalancing: 
