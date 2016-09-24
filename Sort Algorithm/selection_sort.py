# encoding=utf-8
# date: 2016-09-13
# gaooz.com
# 选择排序

def selection_sort(arr):
    for i in range(len(arr)-1, 0, -1):
        index = i
        for j in range(i-1, -1, -1):
            if arr[j] > arr[index]:
                index = j
        if index != i:
            temp = arr[i]
            arr[i] = arr[index]
    return arr

