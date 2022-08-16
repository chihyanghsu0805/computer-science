# Load Balancing

Spread the traffic across to improve responsiveness and availability.
Software (HAProxy) and hardware.

-   Between user and web server
-   Between web server and platform layers, e.g. application servers, cache servers
-   Between platform layer and database

## Benefits
-   Prevent request from going to inhealthy servers
-   Prevent overloading resources
-   Redundant load balancer to alleviate single point of failure
-   SSL termination
-   Session persistence

## Algorithms
-   Healthy Checks

-   Selection Methods
    -   Least connection
    -   Least response time
    -   Least bandwidth
    -   Round robin
    -   Weighted round robin
    -   IP hash
    -   Layer 4
    -   Layer 7
    