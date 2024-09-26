import itertools
from collections import Counter

class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:       
        count = Counter(nums)
        for value, repeats in count.items():
            if repeats > 2:
                for _ in range(repeats-2):
                    nums.remove(value)
        print(nums)
        return len(nums)


if __name__ == "__main__":
    Solution().removeDuplicates([0,0,1,1,1,1,2,3,3])