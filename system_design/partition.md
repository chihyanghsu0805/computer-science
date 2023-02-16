# Data Partitioning

Splitting up a database/table to improve manageability, performance, availability and load balancing.

Scale horizonatally.

## Methods
-   Horizontal partitioning (Data sharding):
    -   same schema
    -   range based partitioning
    -   may lead to unbalanced servers
    -   select sharding key that can evenly distribute data
    -   resharding ([Consistent Hashing](./consistent.md))
    -   celebrity
    -   Join and denormalization ([LINK](./sql.md#scaling-relational-database))

-   Vertical partitioning
    -   store tables related to specific features
    -   may be necesary to further partition
    -   may get up to 24TB according to Amazon Relational Database Service
    -   SPOF
    -   Cost

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
