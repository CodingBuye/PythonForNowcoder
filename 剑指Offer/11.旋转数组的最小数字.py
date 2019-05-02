"""
题目描述
把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。
输入一个非减排序的数组的一个旋转，输出旋转数组的最小元素。
例如数组{3,4,5,1,2}为{1,2,3,4,5}的一个旋转，该数组的最小值为1。
NOTE：给出的所有元素都大于0，若数组大小为0，请返回0。
"""


# class Solution:
#     def minNumberInRotateArray(self, rotateArray):
#         if len(rotateArray) == 0:
#             return 0
#         minor = rotateArray[0]
#         left = 0
#         right = len(rotateArray)-1
#         while left <= right:
#             mid = left + (right-left) // 2
#             if rotateArray[mid] > minor:
#                 left = mid+1
#             elif rotateArray[mid] < minor:
#                 minor = rotateArray[mid]
#                 right = mid - 1
#             else:
#                 left += 1
#         return minor


class Solution:
    def minNumberInRotateArray(self, rotateArray):
        # write code here
        if rotateArray is None or len(rotateArray) == 0:
            return 0
        index1 = 0
        index2 = len(rotateArray) - 1
        index_mid = index1
        while rotateArray[index1] >= rotateArray[index2]:
            if index2 - index1 == 1:
                index_mid = index2
                break
            index_mid = index1 + (index2 - index1) // 2

            if rotateArray[index1] == rotateArray[index2] == rotateArray[index_mid]:
                return self.min_in_order(rotateArray, index1, index2)

            if rotateArray[index_mid] >= rotateArray[index1]:
                index1 = index_mid
            elif rotateArray[index_mid] <= rotateArray[index2]:
                index2 = index_mid
        return rotateArray[index_mid]

    def min_in_order(self, rotateArray, index1, index2):
        res = rotateArray[index1]
        for i in range(index1 + 1, index2 + 1):
            if res > rotateArray[i]:
                res = rotateArray[i]
        return res


rotate = [-1, 4, 5, 0, 7]
Solution().minNumberInRotateArray(rotate)
