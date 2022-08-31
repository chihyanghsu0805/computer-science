#   SQL v.s. NoSQL

## High Level Difference

-   Storage: SQL(Table), NoSQL(various)
-   Schema: SQL(fixed, can be altered offline), NoSQL(dynamic, on the fly)
-   Querying: SQL(Structure Query Language), NoSQL(Unstructured Query Language, different syntax)
-   Scalability: SQL(vertical), NoSQL(horizontal)
-   Reliability, ACID(Atomic, COnsistency, Isolation, Durability): Relational databases are ACID compliant. Most of NoSQL sacrifice ACID for performance and scalability.


## Reasons to use SQL

-   ACID
-   Structured data and unchanged

## Reasons to use NoSQL

-   Big data with no structure
-   Cloud based
-   Rapid development

##  Relational, SQL

-   structured, predefined schema
-   rows and columns
-   MySQL, Oracle, SQLite, Postgres, MariaDB

##  Non-relational, NoSQL

-   unstructured, distributed, dynamic schema
-   Key-value Stores:
    -   Key is an attribute name linked to a value
    -   Redis, Voldemort, Dynamo
-   Document Databases:
    -   data stored in documents and grouped in collections, documents can have entirely different structures
    -   CouchDB, MongoDB

-   Wide Column Databases:
    -   Column families
    -   Large datasets
    -   Cassandra, HBase

-   Graph Databases:
    -   Garph with nodes, properties, and lines
    -   Neo4J, InfiniteGraph



