# encoding=utf-8
# date:2016-09-25
# gaooz.com
# Huffman树-huffman编码-前缀编码

# 利用huffman算法构造Huffman-tree
# 用huffman树表示前缀编码

''' test
from binary_tree_iterate import *
'''

# 树节点结构
class TreeNode(object):
    def __init__(self, data, left = None, right = None):
        self._data = data
        self._left = left
        self._right = right

# 构造huffman树
def huffman_tree(arr):
    nodes = []
    # 构造huffman中所有的叶子节点
    for i in range(len(arr)):
        node = TreeNode(arr[i])
        nodes.append(node)
    # 利用堆排序进行升序排序
    nodes  = heap_sort(nodes)
    while len(nodes) != 1:
        # 选出两个较小的节点
        first_min = nodes.pop(0)
        second_min = nodes.pop(0)
        # 两个较小节点的值构成其父节点的值
        parent = TreeNode(first_min._data+second_min._data, first_min, second_min)
        # 将父节点加入原来的节点序列中(放在第一个堆根位置)
        nodes.insert(0, parent)
        # 再次进行排序
        nodes = heap_sort(nodes)

    # 返回huffman树
    return nodes[0]

# huffman编码（每个字符的huffman编码）
def huffman_code(root):
    '''
       可以利用递归先序遍历求取每个叶子节点的huffman code
       代码略了
    '''
    pass

###########################################################
# 下面是用到的改编后的堆排序（对树节点进行排序）

def build_heap(nodes):
    index = len(nodes)/2 - 1
    for i in range(index, -1, -1):
        heapify(nodes, i)

def heapify(nodes, index):
    # 叶子节点不用做堆调整
    if index <= len(nodes)/2 - 1:
        max_index = index
        if 2*index+1 < len(nodes) and nodes[2*index+1]._data > nodes[max_index]._data:
            max_index = 2*index + 1
        if 2*index+2 < len(nodes) and nodes[2*index+2]._data > nodes[max_index]._data:
            max_index = 2*index + 2
        if nodes[max_index]._data != nodes[index]._data:
            temp = nodes[index]
            nodes[index] = nodes[max_index]
            nodes[max_index] = temp
            heapify(nodes, max_index)

def heap_sort(nodes):
    build_heap(nodes)
    nodes_sorted = []
    while len(nodes) != 0:
        temp = nodes[0]
        nodes[0] = nodes[len(nodes)-1]
        nodes[len(nodes)-1] = temp
        nodes_sorted.insert(0, nodes.pop(len(nodes)-1))
        heapify(nodes, 0)

    return nodes_sorted

''' test

if __name__ == "__main__":
    arr = [1,2,3,4,5]
    root = huffman_tree(arr)
    LoopIterate(root)

'''





