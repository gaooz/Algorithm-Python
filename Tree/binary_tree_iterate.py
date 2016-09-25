# encoding=utf-8
# date:2016-09-25
# gaooz.com
# 二叉树遍历

###################################################

# 递归遍历

###################################################

# 二叉树节点定义
class TreeNode(object):
    def __init__(self, data = -1, left = None, right = None):
        self._data = data
        self._left = left
        self._right = right

# 先序遍历-递归
def PreOrderIterate_Recurse(tree):
    if tree is not None:
        print tree._data,
        PreOrderIterate_Recurse(tree._left)
        PreOrderIterate_Recurse(tree._right)

# 中序遍历-递归
def MidOrderiterate_Recurse(tree):
    if tree is not None:
        MidOrderiterate_Recurse(tree._left)
        print tree._data,
        MidOrderiterate_Recurse(tree._right)

# 后序遍历-递归
def LastOrderIterate_Recurse(tree):
    if tree is not None:
        LastOrderIterate_Recurse(tree._left)
        LastOrderIterate_Recurse(tree._right)
        print tree._data,

###################################################

# 非递归遍历

###################################################

# 先序遍历-非递归
def PreOrderIterate_unRecurse(tree):
    if tree is None:
        return
    # 使用栈进行非递归遍历
    stack_tree = []
    # 根节点进栈
    stack_tree.append(tree)
    while len(stack_tree) != 0:
        # 出栈一个节点
        tree_node = stack_tree.pop(len(stack_tree)-1)
        # 访问该节点
        print tree_node._data,
        # 依次将其右孩子和左孩子进栈
        if tree_node._right is not None:
            stack_tree.append(tree_node._right)
        if tree_node._left is not None:
            stack_tree.append(tree_node._left)

# 中序遍历-非递归
def MidOrderIterate_unRecurse(tree):
    if tree is None:
        return
    # 定义栈
    stack_tree = []
    # 根入栈
    stack_tree.append(tree)
    # 遍历指针
    p = tree._left
    while p is not None or len(stack_tree) != 0:
        if p is not None:
            stack_tree.append(p)
            p = p._left # 一直找到根节点最左边的节点
        else:
            p = stack_tree.pop(len(stack_tree)-1) # 出栈
            print p._data, # 访问该节点
            p = p._right # 遍历右子树

# 后序遍历-非递归
def LastOrderIterate_unRecurse(tree):
    if tree is None:
        return
    stack_tree = []
    # 进栈前先设置根节点的右子树未被访问，下面会用到
    tree._flag = False
    stack_tree.append(tree)
    p = tree._left
    while p is not None or len(stack_tree) != 0:
        if p is not None:
            p._flag = False
            stack_tree.append(p)
            p = p._left
        else:
            if stack_tree[len(stack_tree)-1]._flag is False: # 未遍历过该节点的右子树
                p = stack_tree[len(stack_tree)-1]
                p._flag = True
                p = p._right # 访问右子树
            else: # 已经遍历过该节点的右子树
                # 因为该节点其右子树已经遍历过所以该节点不再使用，直接出栈
                q = stack_tree.pop(len(stack_tree)-1)
                print q._data,


# 层次遍历-利用队列实现
def LoopIterate(tree):
    if tree is None:
        return
    # 定义队列结构（利用列表模拟队列）
    queue = []
    queue.append(tree)
    while len(queue) != 0:
        # 访问队首元素，并将队首元素出队
        p = queue.pop(0)
        print p._data,
        if p._left is not None:
            queue.append(p._left)
        if p._right is not None:
            queue.append(p._right)

''' test

if __name__ == "__main__":
    left = TreeNode(2)
    right = TreeNode(3)
    root = TreeNode(1, left, right)

    left_right = TreeNode(4)
    right_left = TreeNode(5)

    left._right = left_right
    right._left = right_left

    print "PreOrder_recurse："
    PreOrderIterate_Recurse(root)
    print
    print "MidOrder_recurse："
    MidOrderiterate_Recurse(root)
    print
    print "LastOrder_recurse："
    LastOrderIterate_Recurse(root)
    print
    ###############################
    print "PreOrder_unRecurse:"
    PreOrderIterate_unRecurse(root)
    print
    print "MidOrder_unRecurse："
    MidOrderIterate_unRecurse(root)
    print
    print "LastOrder_unRecurse："
    LastOrderIterate_unRecurse(root)
    print
    print "LoopIterate："
    LoopIterate(root)

'''


