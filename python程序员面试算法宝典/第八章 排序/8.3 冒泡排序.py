class Solution:
    def bubble_sort(self, arr):
        """
        :param arr: 待排序数组
        :return: 排序后的数组
        """
        arr_len = len(arr)
        for i in range(0, arr_len - 1):
            for j in range(i + 1, arr_len):
                if arr[i] > arr[j]:
                    arr[i], arr[j] = arr[j], arr[i]
        return arr


if __name__ == "__main__":
    num = [3, 4, 2, 8, 9, 5, 1]
    res = Solution().bubble_sort(num)
    print(res)
