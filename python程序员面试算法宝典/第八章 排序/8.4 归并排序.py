class Solution:
    def merge_sort(self, lists):
        if len(lists) <= 1:
            return lists
        num = len(lists) // 2
        left = self.merge_sort(lists[:num])
        right = self.merge_sort(lists[num:])
        return self.merge(left, right)

    def merge(self, left, right):
        i, j = 0, 0
        res = []
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                res.append(left[i])
                i += 1
            else:
                res.append(right[j])
                j += 1
        res.extend(left[i:])
        res.extend(right[j:])
        return res


if __name__ == '__main__':
    arr = [3, 4, 2, 8, 9, 5, 1]
    res = Solution().merge_sort(arr)
    print(res)
