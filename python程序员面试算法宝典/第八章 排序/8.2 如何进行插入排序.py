def insert_sort(lists):
    num = len(lists)
    for i in range(1, num):
        after = lists[i]
        pre = i - 1
        while pre >= 0:
            if after < lists[pre]:
                lists[pre+1] = lists[pre]
                lists[pre] = after
            pre -= 1
    return lists


if __name__ == '__main__':
    arr = [3, 4, 2, 8, 9, 5, 1]
    print(insert_sort(arr))
