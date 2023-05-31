# Data Partitioning

Splitting up a database/table to improve manageability, performance, availability and load balancing

Scale horizontally

## Methods

-   Horizontal partitioning (Data sharding)
    -   same schema
    -   range based partitioning
    -   may lead to unbalanced servers
    -   select sharding key that can evenly distribute data

-   Vertical partitioning
    -   store tables related to specific features
    -   may be necessary to further partition
    -   may get up to 24TB according to Amazon Relational Database Service
    -   Single Point Of Failure
    -   Cost

-   Directory-Based Partitioning
    -   directory server that holds the mapping between each tuple key to its database server.

## Criteria

-   Key or Hash-Based
    -   uniform allocation
    -   number of database servers is fixed, when adding new servers hashing changes
    -   workaround is [Consistent Hashing](./consistent.md).

-   List Partitioning
    -   each partition is assigned a list of values
    -   lookup values in each partition

-   Round Robin
    -    i mod n

-   Composite

## Problems

-   [Joins and Denormalization](./sql.md#scaling-relational-database)
    -   Joins on a partitioned database is often not feasible
    -   workaround is denormalize but suffers data inconsistency

-   Referential Integrity
    -   intregrity of data can be difficult

-   Rebalancing
    -   uneven distribution
    -   celebrity
