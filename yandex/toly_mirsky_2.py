from typing import List

class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        res = -1
        for i, _ in enumerate(nums):
            left_sum = sum(nums[:i])
            right_sum = sum(nums[i+1:])
            if left_sum == right_sum:
                res = i
                break
        return res

    def pivotIndex(self, nums: List[int]) -> int:
        left_sum = 0
        right_sum = sum(nums)
        for i, value in enumerate(nums):
            if left_sum == right_sum - value:
                return i
            left_sum += value 
            right_sum -= value
        return -1 



nums = [2,3,-1,8,4]
nums2 = [4,0]
print(Solution().pivotIndex(nums2))