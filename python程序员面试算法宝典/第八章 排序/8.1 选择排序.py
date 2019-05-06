def select_sort(lists):
    num = len(lists)  # 数组的长度
    for i in range(0, num-1):
        min_index = i
        for j in range(i+1, num):
            if lists[min_index] > lists[j]:
                min_index = j
        lists[min_index], lists[i] = lists[i], lists[min_index]

    return lists


if __name__ == '__main__':
    arr = [3, 4, 2, 8, 9, 5, 1]
    print(select_sort(arr))
