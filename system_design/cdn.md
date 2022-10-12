# Content Delivery Network (CDN)

CDN is a globally distributed network, serving (static) content from locations near to the client. (CloudFront supports dynamic content.)

## Push CDNs
Push CDNs receive updates whenever it occurs on server.

Content is pushed to CDN and URL rewritten to point to CDN.

Sites with small traffic or unfrequent updates work well with push CDNs.

## Pull CDNs
Pull CDNs grab updates when requested, resulting in a slower request until content is cached on CDN.

URL is rewritten to point to CDN.

Time-to-live (TTL) determines how long content is cached. Sites with heavy traffic work well with Pull CDNs.

## Disadvantages
Content might be stale if it is updated before TTL expires it.

URLs need to be changed to point to CDN.

## Considerations

-   Cost
-   Setting cache expiry
-   Fallback
-   Invalidating files
