# Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.
# Example 1:
# Input: nums = [1,2,3,4,5,6,7], k = 3
# Output: [5,6,7,1,2,3,4]
# Explanation:
# rotate 1 steps to the right: [7,1,2,3,4,5,6]
# rotate 2 steps to the right: [6,7,1,2,3,4,5]
# rotate 3 steps to the right: [5,6,7,1,2,3,4]

class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        # Not efficient really:
        # for _ in range(k):
        #     nums.insert(0, nums.pop())

        n = len(nums)
        k = k % n
        rotated = [0] * n

        for i in range(n):
            rotated[(i + k) % n] = nums[i]

        for i in range(n):
            nums[i] = rotated[i]

if __name__ == "__main__":
    arr = [1,2,3,4,5,6,7]
    Solution().rotate(arr, 3)
    print(arr)