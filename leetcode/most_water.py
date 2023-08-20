# Task content:
# https://leetcode.com/problems/container-with-most-water/


class Solution:

    @staticmethod
    def max_area(height: list[int]) -> int:
        max_area = 0
        for main_index, main_item in enumerate(height):
            for minor_index, minor_item in enumerate(height[main_index+1:]):
                h = min(main_item, minor_item)
                w = minor_index + 1
                s = h * w
                max_area = max(max_area, s)
        return max_area

    @staticmethod
    def max_area_gs(height: list[int]) -> int:
        max_s = 0
        left = 0
        right = len(height) - 1
        while left < right:
            current = (right - left) * min(height[left], height[right])
            max_s = max(current, max_s)
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1
        return max_s


test_height = [10, 8, 6, 2, 5, 4, 8, 10, 7]
test_height2 = [2]
print(Solution.max_area(test_height2))
