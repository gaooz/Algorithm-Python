# encoding=utf-8
# date:2016-10-11
# gaooz.com
# 寻找二叉树中指定节点的最近祖先节点

class TreeNode(object):
    def __init__(self, data, left = None, right = None):
        self._data = data
        self._left = left
        self._right = right

def find_least_common_ancestor(T, p1, p2):
    if T is None or T == p1 or T == p2:
        return T
    left = find_least_common_ancestor(T._left, p1, p2)
    right = find_least_common_ancestor(T._right, p1, p2)

    if left is not None and right is not None:
        return T

    return left if left else right

''' test

if __name__ == "__main__":
    p1 = TreeNode(4)
    p2 = TreeNode(5)
    left = TreeNode(2, p1)
    right = TreeNode(3, p2)
    T = TreeNode(1, left, right)

    print find_least_common_ancestor(T, p1, p2)._data

'''