"""
题目描述
统计一个数字在排序数组中出现的次数。
"""


class Solution:
    def GetNumberOfK(self, data, k):
        # write code here
        return data.count(k)


print(Solution().GetNumberOfK([1,2,3,4,4,4,5,6,7], 4))
