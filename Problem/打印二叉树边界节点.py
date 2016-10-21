# encoding=utf-8
# gaooz.com
# 2016-10-21
# 逆时针打印二叉树边界节点

class TreeNode(object):
    def __init__(self, data, left=None, right=None):
        self._data = data
        self._left = left
        self._right = right
        self._flag = None # 节点标记
        self._floor = 0 # 节点所在层次

def inverse_print_edge_node(T):
    if T is None:
        return
    T._flag = "head"
    # 层次遍历二叉树，对每个节点进行标记。边界节点
    queue = [T]
    q = []

    # 层次遍历等到每个节点所在的层次
    while len(queue) != 0:
        node = queue.pop(0)
        if node._left is not None:
            node._left._floor = node._floor + 1
            queue.append(node._left)
        if node._right is not None:
            node._right._floor = node._floor + 1
            queue.append(node._right)
        q.append(node)

    # 树的总层次数
    floors = q[len(q)-1]._floor
    # 根据层次遍历序列，找出边界节点。对边界节点打上标记
    i = 1
    j = 1
    while i < len(q) and j < floors + 1:
        if q[i]._floor == j:
            if q[i-1]._flag is None:
                q[i-1]._flag = "edge"
            if q[i]._flag is None:
                q[i]._flag = "edge"
            j = j + 1
        i = i + 1
    if q[len(q)-1]._flag is None:
        q[len(q)-1]._flag = "edge"

    # 对树根的左子树进行先序遍历，打印有标记的边界节点和叶子节点
    print T._data
    pre_order_traverse(T._left)
    last_order_traverse(T._right)


def pre_order_traverse(T):
    if T is not None:
        if T._flag is not None:
            if T._flag == "edge" or (T._left is None  and T._right is None):
                print T._data
        pre_order_traverse(T._left)
        pre_order_traverse(T._right)

def last_order_traverse(T):
    if T is not None:
        last_order_traverse(T._left)
        last_order_traverse(T._right)
        if T._flag is not None:
            if T._flag == "edge" or (T._left is None  and T._right is None):
                print T._data

'''test
if __name__ == "__main__":
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node4 = TreeNode(4)
    node5 = TreeNode(5)
    node6 = TreeNode(6)
    node1._right = node3
    node2._left = node4
    node2._right = node5
    node4._left = node6

    T = TreeNode(0, node1, node2)
    inverse_print_edge_node(T)
'''















