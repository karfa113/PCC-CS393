from bisect import bisect_right

def max_value(events, k):
    events.sort(key=lambda x: x[1])  # Sort by end day
    n = len(events)
    # Precompute start days for binary search
    start_days = [event[0] for event in events]
    dp = [[0] * (k + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        # Find the last event that ends before the current event starts
        j = bisect_right([events[x][1] for x in range(n)], events[i-1][0] - 1)
        for t in range(1, k + 1):
            # Option 1: skip current event
            dp[i][t] = max(dp[i][t], dp[i-1][t])
            # Option 2: attend current event
            dp[i][t] = max(dp[i][t], dp[j][t-1] + events[i-1][2])
    return dp[n][k]

# Example usage:
events = [
    [1, 3, 4],
    [2, 5, 2],
    [4, 6, 3],
    [7, 8, 5]
]
k = 2
print("Maximum value:", max_value(events, k))