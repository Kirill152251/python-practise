def subarray_sum(nums: list[int], target: int) -> list[int]:
    d = {0: -1}
    current_sum = 0
    for i, value in enumerate(nums):
        current_sum += value
        if current_sum - target in d.keys():
            start_index = d[current_sum - target] + 1
            return [start_index, i]
        else:
            d[current_sum] = i
    return []


nums = [1, 2, 3, 4, 5]
target = 9
print ( subarray_sum(nums, target) )

nums = [-1, 2, 3, -4, 5]
target = 0
print ( subarray_sum(nums, target) )

nums = [2, 3, 4, 5, 6]
target = 3
print ( subarray_sum(nums, target) )

nums = []
target = 0
print ( subarray_sum(nums, target) )



"""
    EXPECTED OUTPUT:
    ----------------
    [1, 3]
    [0, 3]
    [1, 1]
    []

"""
