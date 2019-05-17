"""
题目描述
请设计一个函数，用来判断在一个矩阵中是否存在一条包含某字符串所有字符的路径。
路径可以从矩阵中的任意一个格子开始，每一步可以在矩阵中向左，向右，向上，向下移动一个格子。
如果一条路径经过了矩阵中的某一个格子，则之后不能再次进入这个格子。
例如 a b c e s f c s a d e e 这样的3 X 4 矩阵中包含一条字符串"bcced"的路径，
但是矩阵中不包含"abcb"路径，因为字符串的第一个字符b占据了矩阵中的第一行第二个格子之后，
路径不能再次进入该格子。
"""


class Solution:

    def hasPath(self, matrix, rows, cols, path):
        if not matrix or rows < 1 or cols < 1 or not path:
            return False
        visited = [False]*(rows*cols)

        path_length = 0

        for row in range(rows):
            for col in range(cols):
                if self.is_has_path(matrix, rows, cols, row, col, path, path_length, visited):
                    return True
        return False

    def is_has_path(self, matrix, rows, cols, row, col, path, path_length, visited):

        if len(path) == path_length:
            return True
        has_path = False
        if 0 <= row < rows and 0 <= col < cols and matrix[row*cols+col] == path[path_length] and (not visited[row*cols+col]):
            path_length += 1

            visited[row*cols+col] = True

            has_path = self.is_has_path(matrix, rows, cols, row-1, col, path, path_length, visited) or self.is_has_path(matrix, rows, cols, row, col+1, path, path_length, visited) or self.is_has_path(matrix, rows, cols, row+1, col, path, path_length, visited) or self.is_has_path(matrix, rows, cols, row, col-1, path, path_length, visited)

            if not has_path:
                path_length -= 1
                visited[row*cols+col] = False
        return has_path


if __name__ == '__main__':
    m = ['A', 'B', 'C', 'E', 'S', 'F', 'C', 'S', 'A', 'D', 'E', 'E']
    print(Solution().hasPath(m, 3, 4, 'ABCB'))
