"""
题目描述
在一个二维数组中（每个一维数组的长度相同），
每一行都按照从左到右递增的顺序排序，
每一列都按照从上到下递增的顺序排序。
请完成一个函数，输入这样的一个二维数组和一个整数，
判断数组中是否含有该整数。
"""


class Solution:
    def Find(self, target, array):
        if len(array) == 0 or len(array[0]) == 0:
            return False
        rows = 0
        cols = len(array[0])-1
        while rows < len(array) and cols >= 0:
            if array[rows][cols] == target:
                return True
            elif array[rows][cols] > target:
                cols -= 1
            else:
                rows += 1
        return False


print(Solution().Find(7, []))
