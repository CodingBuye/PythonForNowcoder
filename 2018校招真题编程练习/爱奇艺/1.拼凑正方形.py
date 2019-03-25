"""
题目描述
牛牛有4根木棍,长度分别为a,b,c,d。羊羊家提供改变木棍长度的服务,
如果牛牛支付一个硬币就可以让一根木棍的长度加一或者减一。
牛牛需要用这四根木棍拼凑一个正方形出来,
牛牛最少需要支付多少硬币才能让这四根木棍拼凑出正方形。
"""


class Solution:
    def lowest_cost(self, array):
        cost = 0
        if len(array) == len(set(array)):
            avg = sum(array) // 4
            for i in array:
                cost += abs(i-avg)
            return cost
        else:
            max = 1
            for j in array:
                pass
