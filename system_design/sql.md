#   SQL v.s. NoSQL

## High Level Difference

-   Storage: SQL(Table), NoSQL(various)
-   Schema: SQL(fixed, can be altered offline), NoSQL(dynamic, on the fly)
-   Querying: SQL(Structure Query Language), NoSQL(Unstructured Query Language, different syntax)
-   Scalability: SQL(vertical), NoSQL(horizontal)
-   Reliability, ACID(Atomic, Consistency, Isolation, Durability): Relational databases are ACID compliant. Most of NoSQL sacrifice ACID for performance and scalability.

## Reasons to use SQL

-   ACID
    -   Atomic: Each transaction is all or nothing
    -   Consistency: Any transaction will bring the database from one valid state to another
    -   Isolation: Executing concurrently is the same as if serially
    -   Durability: Once transaction is committed, it stays committed

-   Structured data and unchanged

## Reasons to use NoSQL

-   Big data with no structure
-   Cloud based
-   Rapid development
-   Super low latency
-   Only need to serialize and deserialize
-   Massive amount of data

##  Relational Database Management System (RDBMS), SQL

-   structured, predefined schema
-   rows and columns
-   MySQL, Oracle, SQLite, PostgreSQL, MariaDB

##  Non-relational, NoSQL

-   BASE
    -   Basically available
    -   Soft state
    -   Eventual consistency

-   Unstructured, distributed, dynamic schema

-   Key-value Stores:
    -   Key is an attribute name linked to a value
    -   Redis, Voldemort, DynamoDB

-   Document Databases:
    -   data stored in documents and grouped in collections, documents can have entirely different structures
    -   CouchDB, MongoDB

-   Wide Column Databases:
    -   Column families
    -   Large datasets
    -   Cassandra, HBase

-   Graph Databases:
    -   Graph with nodes, properties, and lines
    -   Neo4J, InfiniteGraph

## Scaling Relational Database

-   [Master-Slave](./cap.md#availability-patterns)
-   [Master-Master](./cap.md#availability-patterns)
-   Federation
    -   Splits up databases by function
    -   Joining is more complex
-   Sharding v.s. [Partitioning](./partition.md)
    -   https://stackoverflow.com/questions/20771435/database-sharding-vs-partitioning
    -   Joining is more complex
-   Denormalization
    -   Improve read performance at the expense of write performance
    -   Redundant data are written to avoid joins
-   SQL Tuning
