"""
题目描述
输入一个整数，输出该数二进制表示中1的个数。
其中负数用补码表示。
"""


class Solution:
     def NumberOf1(self, n):
         if n < 0:
             n = n & 0xffffffff
         k = 0
         while n:
             k += 1
             n = (n-1) & n
         return k


if __name__ == '__main__':
    print(Solution().NumberOf1(9))
