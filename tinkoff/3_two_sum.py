# https://leetcode.com/problems/two-sum/description/
# Array, Hash Table

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        d = {}
        res = []
        for i, v in enumerate(nums):
            # value + diff = target
            diff = target - v # value + diff = target
            if diff not in d:
                d[v] = i
            else:
                res.append(d[diff])
                res.append(i)
        return res
                



if __name__ == "__main__":
    nums = [3,2,4]
    print(Solution().twoSum(nums, 6))