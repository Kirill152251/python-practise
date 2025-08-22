# https://leetcode.com/problems/subarray-sums-divisible-by-k
# Array, Hash Table, Prefix Sum


class Solution:
    def subarraysDivByK(self, nums: list[int], k: int) -> int:
        p = [0] * (len(nums) + 1)
        res = []
        for index, value in enumerate(nums):
            p[index+1] = p[index] + value
        
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                if (p[j+1] - p[i]) % k == 0:
                    res.append(nums[i:j+1])
        return len(res)

    def subarraysDevByKBetterSolution(self, nums: list[int], k: int) -> int:
        prefix_sum = 0
        res = 0
        d = {}
        d[0] = 1
        for item in nums:
            prefix_sum += item
            reminder = prefix_sum % k
            if reminder not in d:
                d[reminder] = 1
            else:
                res += d[reminder]
                d[reminder] += 1
        return res
            


if __name__ == "__main__":
    nums = [4,5,0,-2,-3,1]
    print(Solution().subarraysDevByKBetterSolution(nums, 5))
