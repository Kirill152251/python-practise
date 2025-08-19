# https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array
# Array, Hash Table

class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        hash_set = {item for item in range(1, len(nums)+1)}
        print(hash_set)
        for item in nums:
            if item in hash_set:
                hash_set.remove(item)
        return list(hash_set) 

    def no_extra_space_solution(self, nums: list[int]) -> list[int]:
        for value in nums:
            if (nums[abs(value)-1]) > 0:
                nums[abs(value) - 1] = -1 * nums[abs(value) - 1]
        return [index + 1 for index, value in enumerate(nums) if value > 0]

if __name__ == "__main__":
    nums = [4,3,2,7,8,2,3,1]
    print(Solution().no_extra_space_solution(nums))
