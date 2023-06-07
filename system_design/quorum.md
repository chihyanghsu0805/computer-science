# Quorum

How to make sure replications are consistent?

Quorum is the minimum number of servers on which a ditributed operation needs to be performed successfully, (N // 2 + 1), odd number of nodes recommended due to number for failure allowed

Minimum Read Nodes (R) + Minimum Write Nodes (W) > N --> Quorum

Best performance 1 < r < w < n. because reads are more frequent than writes
