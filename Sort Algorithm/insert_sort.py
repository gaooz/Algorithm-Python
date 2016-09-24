# encoding=utf-8
# date: 2016-09-13
# gaooz.com
# 插入排序

def insert_sort(arr):
    for i in range(1, len(arr)):
        temp = arr[i]
        j = i
        while j >0 and temp < arr[j-1]:
            arr[j] = arr[j-1]
            j = j-1
        arr[j] = temp
    return arr
