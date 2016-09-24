# encoding=utf-8
# date:2016-09-24
# gaooz.com
# 二分查找

# 递归实现
def binary_search_recurse(arr, k, low, high):
    if low <= high:
        mid = (low+high)/2
        if arr[mid] == k:
            return mid
        elif arr[mid] < k:
            return binary_search_recurse(arr, k, mid+1, high)
        else:
            return binary_search_recurse(arr, k, low, mid-1)
    else:
        return -1 # 没找到时返回-1

# 非递归实现
def binary_search_unrecurse(arr, k):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low+high)/2
        if arr[mid] == k:
            return mid
        elif arr[mid] < k:
            low = mid+1
        else:
            high = mid-1
    return -1





