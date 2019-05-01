"""
题目描述:
我们可以用2*1的小矩形横着或者竖着去覆盖更大的矩形。
请问用n个2*1的小矩形无重叠地覆盖一个2*n的大矩形，
总共有多少种方法？
"""


class Solution:
    def rectCover(self, number):
        if number == 0:
            return 0
        res = [1, 2, 3]
        while len(res) <= number:
            res.append(res[-1]+res[-2])
        return res[number-1]


w = Solution().rectCover(4)
print(w)
