from typing import List
import bisect
import collections

# Given a sorted integer array arr, two integers k and x, return the k closest integers to x in the array.
# The result should also be sorted in ascending order.
# Example 2:
# Input: arr = [1,1,2,3,4,5], k = 4, x = -1
# Output: [1,1,2,3]

class Solution:
    def findClosestElements(self, a: List[int], count: int, x: int) -> List[int]: 
        if x < a[0]:
            index = 0
        elif x > a[len(a)-1]:
            index = len(a) - 1
        else:
            index = bisect.bisect_left(a, x)
            if x not in a and abs(x - a[index]) >= abs(x - a[index-1]):
                index -= 1
        left = index
        right = index
        res = collections.deque()
        while len(res) < count:
            left_value = abs(a[left] - x) if left >= 0 else float('inf')
            right_value = abs(a[right] - x) if right < len(a) else float('inf')
            if left_value < right_value:
                res.appendleft(a[left])
                left -= 1
            elif right_value < left_value:
                res.append(a[right])
                right += 1
            else:
                res.appendleft(a[left]) 
                if left == right:
                    right += 1
                left -= 1
        return list(res)

test = [1,1,1,10,10,10]
print(Solution().findClosestElements(test, 1, 9))