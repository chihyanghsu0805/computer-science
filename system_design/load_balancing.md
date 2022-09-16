# Load Balancing

Spread the traffic across to improve responsiveness and availability with software (HAProxy) and hardware.

-   Between user and web server
-   Between web server and platform layers, e.g. application servers, cache servers
-   Between platform layer and database

## Benefits
-   Prevent request from going to unhealthy servers
-   Prevent overloading resources
-   Redundant load balancer to alleviate single point of failure ([active-passive](./cap.md#availability-patterns) or [active-active](./cap.md#availability-patterns))
-   SSL termination
-   Session persistence
-   Helps with horizontal scaling

## Algorithms
-   Healthy Checks

-   Selection Methods
    -   Random
    -   Session / Cookies
    -   Least connection
    -   Least response time
    -   Least bandwidth
    -   Round robin
    -   Weighted round robin
    -   IP hash
    -   Layer 4
        -   Transport layer (IP, ports)
    -   Layer 7
        -   Application layer (header, message, cookies)

## Disadvantages

-   Performance bottleneck
-   May be single point of failure

