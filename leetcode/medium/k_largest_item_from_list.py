class MaxHeap:
    def __init__(self):
        self.heap = []
    
    def parent(self, index):
        return (index - 1) // 2
    
    def left(self, index):
        return index * 2 + 1
    
    def right (self, index):
        return index * 2 + 2

    def swap(self, index1, index2):
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1] 

    def insert(self, value):
        self.heap.append(value)
        current = len(self.heap) - 1
        while current > 0 and self.heap[self.parent(current)] < self.heap[current]:
            self.swap(current, self.parent(current))
            current = self.parent(current)

    def sink_down(self, index):
        max_index = index
        while True:
            left = self.left(index)
            right = self.right(index)

            if left < len(self.heap) and self.heap[left] > self.heap[max_index]:
                max_index = left

            if right < len(self.heap) and self.heap[right] > self.heap[max_index]:
                max_index = right 

            if max_index != index:
                self.swap(max_index, index)
                index = max_index
            else:
                return

    def remove(self):
        if not self.heap:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        max_value = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.sink_down(0)
        return max_value



class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        h = MaxHeap()
        for i in nums:
            h.insert(i)
        res = -1
        for _ in range(k):
            res = h.remove()
        return res

s = Solution()
l = [3,2,1,5,6,4]
import heapq
heapq.heappop()
print(s.findKthLargest(l, 2))