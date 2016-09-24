# encoding=utf-8
# date: 2016-09-19
# gaooz.com
# 堆排序

# 堆构建
def build_heap(arr):
    length = len(arr)
    # 找到最后一个非叶子节点
    index = length/2 - 1
    # 从最后一个非节点开始依次向上做堆调整
    for i in range(index, -1, -1):
        heapify(arr, i)

# 堆调整，这里按大顶堆进行调整
def heapify(arr, index):
    # 叶子节点无须再做堆调整
    if index > len(arr)/2 - 1:
        return None
    max_index = index
    left_child_index = index*2 + 1
    right_child_index = index*2 + 2
    if left_child_index < len(arr) and arr[left_child_index] > arr[max_index]:
        max_index = left_child_index
    if right_child_index < len(arr) and arr[right_child_index] > arr[max_index]:
        max_index = right_child_index

    if arr[max_index] != arr[index]:
        temp = arr[max_index]
        arr[max_index] = arr[index]
        arr[index] = temp
        # 递归调整
        heapify(arr, max_index)

# 堆排序
def heap_sort(arr):
    arr_sorted = []
    # 先构建堆
    build_heap(arr)
    # 交换堆顶元素和堆末尾元素，交换后堆末尾元素为最大值元素
    while len(arr) != 0:
        temp = arr[0]
        arr[0] = arr[len(arr)-1]
        arr[len(arr)-1] = temp
        arr_sorted.insert(0, arr.pop(len(arr)-1))
        # 调整
        heapify(arr, 0)

    return arr_sorted




