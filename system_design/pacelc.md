# PACELC

ACID (Atomic, Consistency, Isolation, Durability) databases (mySQL, Oracle, Microsfot SQL Server) chose consistency.
BASE (Basically Available, Soft-state, Eventually Consitent) databases (MongoDB, Cassandra, Redis) chose availability.

What if there is no network partition?

If there is partition (P): Availability (A) v.s. Consistency (C) Else (E): Latency (L) v.s. Consistency(C).

PA / EL: Dynamo and Cassandra.
PC / EC: BigTable and HBase.
PA / EC: MongoDB.
