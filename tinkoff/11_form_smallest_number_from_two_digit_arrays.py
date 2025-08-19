# https://leetcode.com/problems/form-smallest-number-from-two-digit-arrays
# Array, Hash Table, Enumeration

class Solution:
    def minNumber(self, nums1: list[int], nums2: list[int]) -> int:
        set1 = set(nums1)
        set2 = set(nums2)
        common = set1 & set2
        if common:
            return min(list(common))
        else:
            min1 = min(nums1)
            min2 = min(nums2)
            return int(str(min(min1, min2)) + str(max(min1, min2)))
    
if __name__ == "__main__":
    nums1 = [4,1,3]
    nums2 = [5,3]
    print(Solution().minNumber(nums1, nums2))
