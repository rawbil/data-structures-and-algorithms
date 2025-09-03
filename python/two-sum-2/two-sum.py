"""
Sol:
array of integer nums: nums=[10, 20, 30, 40]
target = 20
Return 2 indices of the values that add up to the target in the array
"""


def two_sum(nums, target):
    # nested loop
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]


my_list = [10, 7, 3, 5, 5]
print(two_sum(my_list, 10))

"""for i in range(len(my_list)):
    for j in range(i + 1, len(my_list)):
        if my_list[i] + my_list[j] == 10:
            print(f"i: {i}, j: {j}")
"""
