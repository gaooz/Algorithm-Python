# encoding=utf-8
# date:2016-09-13
# gaooz.com
# 冒泡排序

def bubble_sort(arr):
    for i in range(len(arr)-1):
        for j in range(i+1, len(arr)):
            if arr[i] > arr[j]:
                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp
    return arr
