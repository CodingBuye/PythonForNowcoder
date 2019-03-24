"""
题目描述
求1+2+3+...+n，
要求不能使用乘除法、for、while、if、else、switch、case等
关键字及条件判断语句（A?B:C）。
"""


class Solution:
    def sum_solution(self, n):
        return sum(list(range(1, n+1)))


print(Solution().sum_solution(3))
