# Given an array of positive integers nums and a positive integer target, return the minimal length of a 
# subarray
#  whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.
# Example 1:
# Input: target = 7, nums = [2,3,1,2,4,3]
# Output: 2
# Explanation: The subarray [4,3] has the minimal length under the problem constraint.
class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        left = 0
        temp_sum = 0
        res = float("inf")
        for right in range(len(nums)):
            temp_sum += nums[right]
            while temp_sum >= target:
                res = min(right - left + 1, res)
                temp_sum -= nums[left]
                left += 1
        return 0 if res == float("inf") else res

if __name__ == "__main__":
    print(Solution().minSubArrayLen(7, [8,8,8,8,8]))