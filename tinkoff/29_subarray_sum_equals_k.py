# https://leetcode.com/problems/subarray-sum-equals-k
# Array, Hash Table, Prefix Sum

class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        res = 0
        d = {}
        d[0] = 1
        pr_sum = 0
        for item in nums:
            pr_sum += item
            if pr_sum - k in d:
                res += d[pr_sum - k]
            if pr_sum not in d:
                d[pr_sum] = 1
            else:
                d[pr_sum] += 1
        return res

        # d = {}
        # res = 0
        # prefix_sum = 0
        # for item in nums:
        #     prefix_sum += item 
        #     if prefix_sum - k == 0:
        #         res += 1
        #     t = k - item
        #     if t not in d:
        #         d[t] = 1
        #     else:
        #         if prefix_sum - t == k:
        #         # if d[t] + prefix_sum == k:
        #             d[t] += 1
        #             res += d[t]

        # return res 


if __name__ == "__main__":
    # nums = [1,2,1,2,1]
    nums = [-1,-1,1]
    print(Solution().subarraySum(nums, 0))
