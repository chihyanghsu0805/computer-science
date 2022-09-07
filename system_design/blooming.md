# Blooming Filters

Tells whether an element may be in a set or definitely is not.

Bloom filter is a bit array of m bits with k different hash functions.

For each element, hash the element and set k bits to 1.

To test, hash the elemnt to get k bits, if any is 0, element is definitely not in set.

