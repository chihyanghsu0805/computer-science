# Key Characteristics

-   Scalability
    -   Horizontal (more servers) v.s. Vertical (more power)
    -   Horizontal scaling is easier to scale dynamically, e.g. Cassandra (NoSQL), MongoDB (NoSQL)
    -   Vertical scaling may involove downtime, e.g. MySQL

-   Reliability
    -   Service not interrupted despite failure
    -   Redundancy, single point of failure

-   Availability
    -   Percentage of time operational under normal conditions
    -   9s:
        -   Three 9s: ~1 minute per day, ~8 hours per year
        -   Four 9s: ~8 seconds per day, ~1 hour per year

-   Reliability v.s. Availability
    -   Reliability is availability over time
    -   A system is reliable, it is available
    -   A system is available not necessarily reliable

-   Efficiency
    -   Response time (latency) and throughput (bandwidth)

-   Serviceability of Manageability