# Caching

Short term memory, limited but fast, often found a level nearest to front end.

Cache misses: global cache and distributed cache.

Cache hit

## Content Delivery/Distribution Network (CDN)
-   Static media

## Cache Invalidation

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