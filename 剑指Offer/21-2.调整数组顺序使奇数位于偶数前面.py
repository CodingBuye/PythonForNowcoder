"""
题目描述
输入一个整数数组，实现一个函数来调整该数组中数字的顺序，
使得所有的奇数位于数组的前半部分，所有的偶数位于数组的后半部分，
并保证奇数和奇数，偶数和偶数之间的相对位置不变。
"""


class Solution:
    def reOrderArray(self, array):
        if len(array) == 1:
            return array[0]
        odd, even = [], []
        for i in array:
            if i % 2 == 0:
                even.append(i)
            else:
                odd.append(i)
        odd.extend(even)
        return odd

    def re_order_array(self, array):
        # 借助插入排序的思想
        k = 0
        for i in range(len(array)):
            if array[i] % 2 == 1:
                j = i
                while j > k:
                    array[j], array[j-1] = array[j-1], array[j]
                    j -= 1
                k += 1
        return array


if __name__ == '__main__':
    a = [1,3,6,8,2,4,7]
    print(Solution().re_order_array(a))
