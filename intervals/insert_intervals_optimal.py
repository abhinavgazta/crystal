def insert_interval(intervals, newInterval):
    result = []
    i = 0
    n = len(intervals)

    # Add intervals that end before newInterval starts
    while i < n and intervals[i][1] < newInterval[0]:
        result.append(intervals[i])
        i += 1

    # Merge overlapping intervals
    while i < n and intervals[i][0] <= newInterval[1]:
        newInterval[0] = min(newInterval[0], intervals[i][0])
        newInterval[1] = max(newInterval[1], intervals[i][1])
        i += 1
    result.append(newInterval)

    # Add the remaining intervals
    while i < n:
        result.append(intervals[i])
        i += 1

    return result


# Example usage:
intervals = [[1, 3], [6, 9]]
newInterval = [2, 5]
print(insert_interval(intervals, newInterval))  # Output: [[1,5],[6,9]]
