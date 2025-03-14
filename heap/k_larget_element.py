import heapq

# log n solution as it does not involve sorting..
# solved via direclty using algos only..
# O( n log k ) ... v/s O ( n log n ) as heap is log k. where k is size of heap..
'''
    Initialize an empty min-heap.
    Insert elements into the heap:
    If the size of the heap exceeds k, remove the smallest element using heappop.
    This ensures that the heap always contains the largest k elements.
    The smallest element in the heap (heap[0]) will be the kth largest element.
'''
def find_min_k(arr, k):
    min_heap = []
    for elem in arr:
        heapq.heappush(min_heap, elem)
        print("min heap", min_heap)
        if len(min_heap) > k:
            print("popping element")
            heapq.heappop(min_heap)
            print("updated min heap", min_heap)
    print("ans is ", min_heap[0])

arr = [12, 3, 9, 10]
arr = [3,2,1,5,6,4]
k = 3
find_min_k(arr, k)


def findKthLargest(nums, k):
    min_heap = []
    for num in nums:
        heapq.heappush(min_heap, num)
        if len(min_heap) > k:
            heapq.heappop(min_heap)  # Remove the smallest element to keep heap size at k
    return min_heap[0]  # The root of the heap is the kth largest element

# Example usage
nums = [3,2,1,5,6,4]
k = 2
print(findKthLargest(nums, k))  # Output: 5

nums = [3,2,3,1,2,4,5,5,6]
k = 4
print(findKthLargest(nums, k))
