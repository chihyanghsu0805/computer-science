# Consistency, Availability, Partition Tolerance

-   Consistency: All nodes see the same data at the same time
-   Availability: Every request received by a non-failing node must respond, may not be the most recent data
-   Partition tolerance: A partition is a communication break between any two nodes

-   CA: RDBMS (Relational Database Management System)
-   CP: Requires atomic reads and writes, BigTable, HBase.
-   AP: Eventual consistency, Dynamo, Cassandra, CouchDB.

## Consistency Patterns

-   Weak Consistency:
    -   Reads may not see the most recent write
    -   Memcached

-   Eventual Consistency:
    -   Reads eventually sees the write, data replicates asynchronously
    -   Email, highly available systems.

-   Strong Consistency:
    -   Reads will see the write, data replicates synchronously
    -   File systems, RDBMs, systems that need transactions

## Availability Patterns

-   Fail-Over:
    -   Active-Passive:
        -   Heartbeats are sent between the active
        -   If the heartbeat is interrupted, passive takes over
        -   Hot or Cold standby
        -   Master-Slave

    -   Active-Active:
        -   Both servers are managing traffic
        -   Master-Master

    -   Disadvantages:
        -   More hardware and complexity
        -   Potential loss of data if active fails before replicate to passive

-   Replication:
    -   Master-Slave: Master reads and writes, Slave reads
    -   Master-Master: loosely consistent (violating ACID) or increased latency
    -   Disadvantages:
        -   Potential data loss
        -   Lot of writes may bogged down reads
        -   More slaves, more replicates

## Availability in Numbers

-   99.9:
    -   8h 45m 57s / y
    -   43m 49.7s / m
    -   10m 4.8s / w
    -   1m 26.4s / d

-   99.99:
    -   52m 35.7s / y
    -   4m 23s / m
    -   1m 5s / w
    -   8.6s / d
