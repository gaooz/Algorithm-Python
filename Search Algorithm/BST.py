# encoding=utf-8
# date:2016-09-28
# gaooz.com
# 二叉查找树

''' test
from Tree.binary_tree_iterate import *
'''

# 二叉树节点定义
class TreeNode(object):
    def __init__(self, data, left = None, right = None):
        self._data = data
        self._left = left
        self._right = right

# 在基本的二叉查找树T中搜索某个元素key
def search_BST(T, key):
    if T is not None:
        if T._data == key:
            return T
        elif T._data > key:
            return search_BST(T._left, key)
        else:
            return search_BST(T._right, key)
    else:
        return None

# 向二叉查找树中插入节点的过程
# P是T的父节点
def insert_BST(P, T, key):
    if T is not None:
        if T._data == key:
            return T
        elif T._data > key:
            return insert_BST(T, T._left, key)
        else:
            return insert_BST(T, T._right, key)
    elif P is not None:
        if P._data > key:
            P._left = TreeNode(key)
            return P._left
        elif P._data < key:
            P._right = TreeNode(key)
            return P._right
        else:
            return P
    else:
        return TreeNode(key)

# 向二叉查找树中删除节点的过程
def delete_BST(T, key):
    # 首先查找到key所在的节点
    p = T
    f = T
    while p is not None  and p._data != key:
        f = p
        if p._data > key:
            p = p._left
        elif p._data < key:
            p = p._right
    # 执行删除节点操作
    if p is not None:
        # 左右子树为空的情况
        if p._left is None and p._right is None:
            if f._data > p._data:
                f._left = None
            else:
                f._right = None
            del p
        # 只有左子树的情况
        elif p._right is None:
            if p._data > f._data:
                f._right = p._left
            else:
                f._left = p._left
            del p
        # 只有右子树的情况
        elif p._left is None:
            if p._data > f._data:
                f._right = p._right
            else:
                f._left = p._right
            del p
        # 左右子树都不为空的情况
        else:
            # 找到p左子树中最大的节点s,q是s的父亲节点
            s = p._left
            q = s
            while s._right is not None:
                q = s
                s = s._right
            # 置换p
            p._data = s._data
            if q != p:
                q._right = s._left
            else:
                q._left = s._left
            del s
    return T

''' test

if __name__ == "__main__":
    T = TreeNode(2, TreeNode(1), TreeNode(3))
    print search_BST(T, 1)._data

    print insert_BST(None, T, 4)._data

    PreOrderIterate_unRecurse(T)

    delete_BST(T, 4)
    print
    PreOrderIterate_unRecurse(T)

'''

