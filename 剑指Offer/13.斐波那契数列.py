"""
大家都知道斐波那契数列，现在要求输入一个整数n，
请你输出斐波那契数列的第n项（从0开始，第0项为0）。
n<=39
"""


class Solution:
    def Fibonacci(self, n):
        if n == 0 or n == 1:
            return n
        res = [1, 2]
        while len(res) <= n:
            res.append(res[-1]+res[-2])
        return res[n-2]


w = Solution().Fibonacci(3)
print(w)
