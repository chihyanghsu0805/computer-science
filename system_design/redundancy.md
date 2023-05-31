# Redundancy and Replication

## Redundancy
Increasing reliability via duplication, removing single points of failure (SPOF)

## Replication
Ensure consistency between redundant resources to improve reliability, fault tolerance, or accessibility

Primary -> Replica

Master generally only supports write operations

Slave gets copies from master and generally only supports read operations

Most applications are usually more reads than writes so slaves are usually more than masters

If Master goes down, a slave can be promoted as master. But data may not be up to date
