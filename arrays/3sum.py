
def three_sum(nums):
    nums.sort()  # Sort the array to handle duplicates easily
    result = []
    n = len(nums)

    for i in range(n - 2):
        if i > 0 and nums[i] == nums[i - 1]:  # Skip duplicate elements
            continue

        left, right = i + 1, n - 1  # Two-pointer approach
        while left < right:
            total = nums[i] + nums[left] + nums[right]

            if total == 0:
                result.append([nums[i], nums[left], nums[right]])

                # Move both pointers to avoid duplicates
                left += 1
                right -= 1
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1

            elif total < 0:
                left += 1  # Increase the sum
            else:
                right -= 1  # Decrease the sum

    return result


# Example usage
nums = [-1, 0, 1, 2, -1, -4]
print(three_sum(nums))

if __name__ == '__main__':
    nums = [-1, 0, 1, 2, -1, -4]
    three_sum(nums)
    #  ans is [ -1, -1, 2], [-1, 0, 1]