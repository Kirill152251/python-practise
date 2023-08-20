class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        j = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                nums[j] = nums[i]
                j += 1
        return j
    
print(Solution.removeDuplicates(Solution, [4,15,15]))