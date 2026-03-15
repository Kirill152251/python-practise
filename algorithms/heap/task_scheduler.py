import heapq
from typing import List


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        h = {}
        for i in tasks:
            h[i] = h.get(i, 0) - 1
        counts = list(h.values())
        heapq.heapify(counts)
        q = []
        time = 0
        while q or counts:
            time += 1
            if counts:
                task = 1 + heapq.heappop(counts)
                if task != 0:
                    q.append((task, time + n))
            if q and q[0][1] == time:
                heapq.heappush(counts, q.pop(0)[0])
        return time
        
    

tasks = ["A","A","A","B","B","B"]

tasks_2 = ["A","C","A","B","D","B"]
print(Solution().leastInterval(tasks_2, 1))
print(Solution().leastInterval(tasks, 2))