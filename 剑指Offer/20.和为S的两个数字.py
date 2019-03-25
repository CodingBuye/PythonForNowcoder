"""
题目描述
输入一个递增排序的数组和一个数字S，
在数组中查找两个数，使得他们的和正好是S，
如果有多对数字的和等于S，输出两个数的乘积最小的。

输出描述:
对应每个测试案例，输出两个数，小的先输出。
"""


class Solution:
    def FindNumberWithSum(self, array, tsum):
        res = []
        for i in range(len(array)-1):
            for j in range(i+1, len(array)):
                if array[i]+array[j] == tsum:
                    res.append((array[i], array[j], array[i]*array[j]))
        if len(res) == 0:
            return []
        minus = res[0][2]
        keep = 0
        for (index, i) in enumerate(res):
            if i[2] < minus:
                minus = i[2]
                keep = 0
        return [res[keep][0], res[keep][1]]


s = Solution().FindNumberWithSum([1, 2, 3, 4], 5)
print(s)
