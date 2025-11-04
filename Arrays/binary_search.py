def binary_search(nums, target):
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1  # this should be outside the loop


numbers = [2, 3, 5, 7, 9, 11, 16, 19, 20, 28, 43, 51, 55, 56, 71, 75]
target_value = 51

index = binary_search(numbers, target_value)

if index != -1:
    print(f"Value {target_value} found at index {index}")
else:
    print("Target not found in array.")
