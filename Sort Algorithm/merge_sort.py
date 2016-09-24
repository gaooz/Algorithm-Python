# encoding=utf-8
# date: 2016-09-22
# gaooz.com
# 归并排序

# 归并
def merge(list, left, mid, right):
    i = left
    j = mid + 1
    temp = []
    while i <= mid and j <= right:
        if list[i] < list[j]:
            temp.append(list[i])
            i = i+1
        else:
            temp.append(list[j])
            j = j+1
    while i <= mid:
        temp.append(list[i])
        i = i+1
    while j <= right:
        temp.append(list[j])
        j = j+1

    # 将临时表中数据复制到原理的表中
    index = range(left, right+1)
    for i in range(len(temp)):
        list[index[i]] = temp[i]

# 归并排序
def merge_sort(arr, left, right):
    if left < right:
        # 划分
        mid = (left+right)/2
        merge_sort(arr, left, mid)
        merge_sort(arr, mid+1, right)
        # 归并
        merge(arr, left, mid, right)
