# Task content:
# https://leetcode.com/problems/container-with-most-water/


class Solution:

    @staticmethod
    def max_area(height: list[int]) -> int:
        max_v = 0
        size = len(height)
        for main_index, main_item in enumerate(height):
            for minor_index, minor_item in enumerate(height[main_index+1:]):
                h = min(main_item, minor_item)
                w = minor_index + 1
                v = h * w
                # print(f'height = {h}, width = {w}')
                # print(f'volume = {h * w}\n')
                max_v = max(max_v, v)
        return max_v


test_height = [10, 8, 6, 2, 5, 4, 8, 10, 7]
test_height2 = [1, 7, 4, 2]
print(Solution.max_area(test_height))
