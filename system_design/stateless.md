# Stateless Web Tier

To scale the web tier horizontally, move state out of the web tier.

## Stateful server

Stateful server remembers client data.

Requests from the same user must be routed to the same server.

This can be done by sticky sessions in load balancers.

Adding / removing servers and handling server failure is difficult.

## Stateless server

State data is fetched from a shared data store, usually NoSQL since it is easy to scale.

Autoscaling refers to adding / removing servers automatically based on traffic.
