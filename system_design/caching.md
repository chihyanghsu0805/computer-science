# Caching

Short term memory, limited but fast, often found a level nearest to front end.

Cache misses: global cache and distributed cache.

Cache hit

Avoid file based caching.

-   Client
-   [CDN](./cdn.md)
-   [Web Server](./proxies.md#reverse-proxy)
-   Database
-   Application
-   Database Query
    -   Hard to delete
    -   If a data changes, all queries need to be deleted
-   Object Level
    -   Remove the object when data changed
    -   Allows asynchronous processing
    -   User sessions, fully rendered webpages, activity streams, user graph data

## Cache invalidation

If data is modified in database, it should be invalidated in the cache.

-   Write through cache: data write into cache and database simultaneously, complete data consistency, higher latency

-   Write around cache: data write to storage bypassing the cache, may result in cache miss and experience higher latency

-   Write back cache: data wriiten to cache before storage, low latency and hight throughput, risks data loss

## Cache eviction policies

-   FIFO
-   LIFO
-   Least Recently Used
-   Moset Recently Used
-   Least Frequently Used
-   Random Replacement

## Cache update
-   Cache aside (Memcache)
    -   Look in cache -> Cache miss -> Look in database -> Add to cache -> Return
    -   Delay, Data may be stale (TTL)
-   Write through
    -   Write to cache -> write to database -> return
    -   Slow due to write
-   Write behind (back)
    -   Write to cache -> asynchronous write to database (add event to queue) -> return
    -   Data loss
-   Refresh ahead
    -   Automatically refresh recently accessed cache entry prior to expiration
    -   Inaccurate prediction results in reduced performance

