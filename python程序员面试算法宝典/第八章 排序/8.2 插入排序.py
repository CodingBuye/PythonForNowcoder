"""
对于给定一组记录，初始时假设第一个记录自成一个有序序列，其余的记录为无序序列；
接着从第二个记录开始，按照记录的大小依次将当前处理的记录插入到其之前的有序序列中，
直到最后一个记录插入到有序序列中为止。
"""


class Solution:
    def insert_sort(self, arr):
        """
        :param arr: 待排序数组
        :return: 排序后的数组
        """
        if not arr:
            return []
        arr_len = len(arr)
        for i in range(1, arr_len):
            val = arr[i]
            j = i-1
            while j >= 0:
                if arr[j] > val:
                    arr[j+1] = arr[j]
                    arr[j] = val
                j -= 1
        return arr


if __name__ == "__main__":
    nums = [3, 4, 2, 8, 9, 5, 1]
    res = Solution().insert_sort(nums)
    print(res)
