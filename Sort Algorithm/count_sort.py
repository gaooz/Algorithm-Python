# encoding=utf-8
# date：2016-09-23
# gaooz.com
# 计数排序

def count_sort(arr, k):
    count = []
    # 初始化count数组
    for i in range(k):
        count.append(0)
    # 计算count数组
    for i in range(len(arr)):
        count[arr[i]] = count[arr[i]] + 1
    # 根据count数组对序列进行排序
    arr_sorted = []
    for key in range(len(count)):
        for key_num in [key for repeat in range(count[key])]:# 列表解析生成j个重复的i
            arr_sorted.append(key_num)
    # 返回排序好的元素序列
    return arr_sorted