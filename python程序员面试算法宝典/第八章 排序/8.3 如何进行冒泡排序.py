def bubble_sort(lists):
    num = len(lists)
    for i in range(0, num-1):
        for j in range(i+1, num):
            if lists[i] > lists[j]:
                lists[i], lists[j] = lists[j], lists[i]
    return lists


if __name__ == '__main__':
    arr = [3, 4, 2, 8, 9, 5, 1]
    print(bubble_sort(arr))
