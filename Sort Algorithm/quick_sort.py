# encoding=utf-8
# date：2016-09-20
# gaooz.com
# 快速排序

def quick_sort(arr, left_index, right_index):
    # 递归终止条件
    if left_index >= right_index:
        return None
    # 选择第一个元素为枢纽节点
    key = arr[left_index]
    # 左下标
    low = left_index
    # 右下标
    high = right_index
    while low < high:
        while low < high and key < arr[high]:
            high = high -1

        # 找到key > arr[high]的元素，交换
        arr[low] = arr[high]

        while low < high and key > arr[low]:
            low = low + 1

        # 找到key < arr[low]的元素，交换
        arr[high] = arr[low]

    # 此时必定low == high
    arr[low]= key
    # 递归排序左半部分序列
    quick_sort(arr, left_index, low-1)
    # 递归排序右半部分序列
    quick_sort(arr, low+1, right_index)
