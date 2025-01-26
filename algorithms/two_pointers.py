from collections import Counter
"""
When to use two_pointers technique?
1. finding pairs or triplets thats satisfy condition
2. reversing array or string in place

When to use sliding window?
1. The problem will be based on an array, list or string type of data structure.
2. It will ask to find subranges in that array to give the longest,
shortest or target values of a string.
3. Its concept is mainly based on ideas like the longest sequence or 
shortest sequence of something that satisfies a given condition perfectly.
"""

def two_sum(arr: list, target: int):
    arr = sorted(arr)
    left, right = 0, len(arr) - 1
    while left < right:
        sum = arr[left] + arr[right]
        if sum == target:
            return (arr[left], arr[right])
        if sum > target:
            right -= 1
        if sum < target:
            left += 1
    return None

def reverse_in_place(word) -> str:
    word = list(word)
    left, right = 0, len(word) - 1
    while left < right:
        word[left], word[right] = word[right], word[left]
        left += 1; right -= 1
    return ''.join(word)

def largest_subarray_sum(arr: list, size: int) -> int:
    if size >= len(arr):
        return sum(arr)
    left, right = 0, size - 1
    m = 0
    while right != len(arr):
        window = arr[left:right + 1]
        window_sum = sum(window)
        m = max(m, window_sum)
        left += 1; right += 1
    return m

def anagram_count(value, target) -> int:
    def is_anagram(s, target) -> bool:
        return Counter(target) == Counter(s)
    
    res = 0
    left, right = 0, len(target) - 1
    while right < len(value):
        window = value[left: right + 1]
        if is_anagram(window, target):
            res += 1
        left += 1; right += 1
    return res

class Solution:
    def trap(self, h: list[int]) -> int:
        res = 0
        left = 0; right = len(h) - 1
        left_max_h = h[left]; right_max_h = h[right]
        while left != right:
            if left_max_h < right_max_h:
                left += 1
                left_max_h = max(left_max_h, h[left])
                res += left_max_h - h[left]
            else:
                right -= 1
                right_max_h = max(right_max_h, h[right])
                res += right_max_h - h[right]
        return res


if __name__ == "__main__":
    data = [0,1,0,2,1,0,1,3,2,1,2,1]
    print(Solution().trap(data))
