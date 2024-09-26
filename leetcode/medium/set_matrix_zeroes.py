# Given an m x n integer matrix matrix, if an element is 0,
# set its entire row and column to 0's.
# You must do it in place.
# Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
# Output: [[1,0,1],[0,0,0],[1,0,1]]

class Solution:

    def setZeroes(self, matrix: list[list[int]]) -> None:
        xs = set()
        ys = set()
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    xs.add(i)
                    ys.add(j)
        for x in xs:
            for y in range(len(matrix[0])):
                matrix[x][y] = 0
        for y in ys:
            for x in range(len(matrix)):
                matrix[x][y] = 0

if __name__ == "__main__":
    arr = [[1,1,1],[1,0,1],[1,1,1]]
    arr = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
    Solution().setZeroes(arr)
    [print(item) for item in arr]