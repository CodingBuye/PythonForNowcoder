"""
地上有一个m行和n列的方格。一个机器人从坐标0,0的格子开始移动，
每一次只能向左，右，上，下四个方向移动一格，
但是不能进入行坐标和列坐标的数位之和大于k的格子。
例如，当k为18时，机器人能够进入方格（35,37），因为3+5+3+7 = 18。
但是，它不能进入方格（35,38），因为3+5+3+8 = 19。
请问该机器人能够达到多少个格子？
"""


class Solution:

    def movingCount(self, threshold, rows, cols):
        # write code here
        if threshold < 0 or rows < 1 or cols < 1:
            return 0
        visited = [False] * (rows * cols)
        num = self.moving_count_core(threshold, rows, cols, 0, 0, visited)
        return num

    def moving_count_core(self, threshold, rows, cols, row, col, visited):
        n = 0
        if self.check(threshold, rows, cols, row, col, visited):
            visited[row*cols+col] = True
            n = 1 + self.moving_count_core(threshold, rows, cols, row-1, col, visited) + self.moving_count_core(threshold, rows, cols, row, col+1, visited) + self.moving_count_core(threshold, rows, cols, row+1, col, visited) + self.moving_count_core(threshold, rows, cols, row, col-1, visited)
        return n

    def check(self, threshold, rows, cols, row, col, visited):
        if 0 <= row < rows and 0 <= col < cols and not visited[row*cols+col] and self.get_digit_sum(row)+self.get_digit_sum(col) <= threshold:
            return True
        return False

    def get_digit_sum(self, num):
        s = 0
        while num > 0:
            s += num % 10
            num = num // 10
        return s


if __name__ == '__main__':
    s = Solution()
    k = s.get_digit_sum(35)
    b = s.movingCount(5, 10, 10)
    print(b)
