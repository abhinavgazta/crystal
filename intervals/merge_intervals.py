'''
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
'''
def merge_intervals(arr):
    if not arr:
        return []

    arr.sort()  # Sort based on start time
    first = [arr[0]]  # Initialize with the first interval
    # start , end bevause array of array..
    for start, end in arr[1:]:
        last_start, last_end = first[-1]
        if start <= last_end:  # Overlapping intervals
            first[-1][1] = max(last_end, end)  # Merge intervals
        else:
            first.append([start, end])  # Add new interval

    print(first)

def insert_intervals(arr, interval):
    if not arr:
        return []
    arr.append(interval)
    arr.sort()  # Sort based on start time
    first = [arr[0]]  # Initialize with the first interval
    # start , end because array of array..
    print(arr)
    # sort this with the merged interval..
    for start, end in arr[1:]:
        last_start, last_end = first[-1]
        if start <= last_end:  # Overlapping intervals
            first[-1][1] = max(last_end, end)  # Merge intervals
        else:
            first.append([start, end])  # Add new interval

    print(first)



arr = [[1,3],[6,9]]
interval = [2, 5]
# arr = [[1,4],[4,5]]
arr = [[10,16],[2,8],[1,6],[7,12]]
arr = [[1,3],[2,6],[8,10],[15,18]]
bot = [[1, 6], [2, 8], [9, 12], [10, 16]]
merge_intervals(bot)
# insert_intervals(arr, interval)