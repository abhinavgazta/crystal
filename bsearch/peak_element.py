from cmath import inf


def find_peak_element(arr):
    # O(n) solns
    peak_elem = -inf
    for i in range(1, len(arr)-1):
        if arr[i] > arr[i-1] and arr[i] > arr[i+1]:
            print("peak element", arr[i])
            peak_elem = max(arr[i], peak_elem)
    print("the final peak elem", peak_elem)
    print("the index is here...", arr.index(peak_elem))

def findPeakElem(arr):
    left , right = 0, len(arr)-1
    while left < right:
        mid = (left + right) // 2
        if arr[mid] < arr[mid+1]:
            # peak is in right half
            left += 1
        else:
            right = mid
    return left
nums = [1,2,3,1]
# nums = [5,6,4,3,1,2,1]
# find_peak_element(nums)
find_peak_element(nums)
print("peaky blinders ans .", findPeakElem(nums))
# ans = 3 is peak element  index = 2 is ans , as 3 > 2 > 1
