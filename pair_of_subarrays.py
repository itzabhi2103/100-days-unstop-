from collections import defaultdict
import bisect
def calculate_pairs(n, arr):
    sum_intervals = defaultdict(list)

    for i in range(n):
        current_sum = 0
        for j in range(i, n):
            current_sum+=arr[j]
            sum_intervals[current_sum].append((i+1, j+1))
    total_count = 0
    for s in sum_intervals:
        intervals = sum_intervals[s]
        if len(intervals)<2:
            continue
        intervals.sort()
        all_ends = sorted([inter[1] for inter in intervals])

        for start, end in intervals:
            count = bisect.bisect_left(all_ends, start)
            total_count+=count
    return total_count
