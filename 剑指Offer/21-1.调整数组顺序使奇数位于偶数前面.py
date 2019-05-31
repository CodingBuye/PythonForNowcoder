"""
题目描述
输入一个整数数组，实现一个函数来调整该数组中数字的顺序，
使得所有的奇数位于数组的前半部分，所有的偶数位于数组的后半部分，
"""


class Solution:
    def reorder_odd_even(self, array):
        if array is None or len(array) < 1:
            return None
        i = 0
        j = len(array) - 1
        while i < j:
            while i < j and array[i] % 2 == 1:
                i += 1

            while i < j and array[j] % 2 != 1:
                j -= 1

            if i < j:
                array[i], array[j] = array[j], array[i]
        return array

    def reorder_odd_even2(self, array):
        if array is None or len(array) < 1:
            return None
        i = 0
        j = len(array) - 1
        while i < j:
            while i < j and self.func(array[i]) is False:
                i += 1

            while i < j and self.func(array[j]) is True:
                j -= 1

            if i < j:
                array[i], array[j] = array[j], array[i]
        return array

    def func(self, n):
        return n % 2 == 0


if __name__ == '__main__':
    print(Solution().reorder_odd_even2([1, 4, 3, 5, 2]))
