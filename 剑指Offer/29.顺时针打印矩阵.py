"""
题目描述
输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字，
例如，如果输入如下4 X 4矩阵：
   1  2   3  4
   5  6   7  8
   9  10 11 12
   13 14 15 16
则依次打印出数字1,2,3,4,8,12,16,15,14,13,9,5,6,7,11,10.
"""


class Solution:
    def print_matrix(self, matrix):
        if matrix is None or len(matrix) < 1 or len(matrix[0]) < 1:
            return None
        rows = len(matrix)
        cols = len(matrix[0])
        start = 0
        res = []
        while rows > start * 2 and cols > start * 2:
            res.extend(self.print_matrix_in_circle(matrix, rows, cols, start))
            start += 1
        return res

    def print_matrix_in_circle(self, matrix, rows, cols, start):
        end_x = cols - start - 1  # 末行坐标
        end_y = rows - start - 1  # 末列坐标
        arr = []
        # 从左到右打印一行
        for i in range(start, end_x + 1):
            arr.append(matrix[start][i])

        # 从上到下打印一行
        if start < end_y:
            for i in range(start + 1, end_y + 1):
                arr.append(matrix[i][end_y])

        # 从右到左打印一行
        if start < end_y and start < end_x:
            for i in range(end_x - 1, start - 1, -1):
                arr.append(matrix[end_y][i])

        # 从下到上打印一行
        if start < end_x and start < end_y:
            for i in range(end_y - 1, start, -1):
                arr.append(matrix[i][start])
        return arr


if __name__ == '__main__':
    m = [[1, 2, 3, 4],
         [5, 6, 7, 8],
         [9, 10, 11, 12],
         [13, 14, 15, 16]]
    r = Solution().print_matrix(m)
    print(r)
