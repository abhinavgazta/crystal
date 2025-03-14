
def max_water_contain(arr):
    left_max = 0
    right_max = len(arr) - 1
    max_water = 0

    while left_max < right_max:
        current_water = min(arr[left_max], arr[right_max]) * (right_max - left_max)
        max_water = max(max_water, current_water)
        
    pass

if __name__ == '__main__':
    # Input: height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    # Output: 49
    pass