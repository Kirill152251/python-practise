import itertools

class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        return [list(item) for item in itertools.combinations(list(range(1,n+1)), k)]

if __name__ == "__main__":
    print(Solution().combine(4, 2))