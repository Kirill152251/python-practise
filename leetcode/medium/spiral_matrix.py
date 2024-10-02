# Spiral Matrix
# Given an m x n matrix, return all elements of the matrix in spiral order.
# Example 1:
# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [1,2,3,6,9,8,7,4,5]
# Example 2:
# Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# Output: [1,2,3,4,8,12,11,10,9,5,6,7]
class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        res = []
        def rotate(matrix: list[list[int]]):
            temp = [[] for _ in range(len(matrix[0]))]
            for x in range(len(matrix[0])-1, -1, -1):
                for y in range(len(matrix)):
                    temp[len(matrix[0])-1-x].append(matrix[y][x])

            return temp

        while True:
            res.extend(matrix.pop(0))
            if not matrix:
                break
            matrix = rotate(matrix) 
        return res
if __name__ == "__main__":
    print(Solution().spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]]))