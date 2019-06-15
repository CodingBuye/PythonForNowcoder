"""
对于给定的一组记录，经过第一轮比后得到最小的记录，然后将该记录与第一个记录交换；
接着对不包括第一个记录以外的其他记录进行第二轮的比较，得到最小的记录并与第二个记录进行位置交换；
重复该过程，直到比较的记录只有一个时为止。
"""


class Solution:

    def select_sort(self, arr):
        """
        :param arr: 待排序的数组
        :return: 排序后的数组
        """
        if not arr:
            return []
        arr_len = len(arr)
        for i in range(arr_len-1):
            min_index = i
            for j in range(i+1, arr_len):
                if arr[j] < arr[min_index]:
                    min_index = j
            arr[i], arr[min_index] = arr[min_index], arr[i]
        return arr


if __name__ == "__main__":
    nums = [3, 4, 2, 8, 9, 5, 1]
    res = Solution().select_sort(nums)
    print(res)
