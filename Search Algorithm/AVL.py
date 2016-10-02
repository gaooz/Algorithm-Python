# encoding=utf-8
# date:2016-09-28
# gaooz.com
# AVL树

# 定义平衡二叉树的节点结构
class TreeNode(object):
    def __init__(self, data, bf = 0, left = None, right = None):
        self._data = data
        self._bf = bf # 该节点的平衡因子
        self._left = left
        self._right = right

# 定义平衡因子取值
LH = 1 # 左子树高
EH = 0 # 左右子树等高
RH = -1 # 右子树高

# 向右旋转
def R_route(P):
    left_child = P._left
    P._left = left_child._right
    left_child._right = P
    # 变为旋转后的新根节点
    return left_child

# 向左旋转
def L_route(P):
    right_child = P._right
    P._left = right_child._left
    right_child = P
    # 变为新的根节点
    return right_child

# 左子树平衡化算法
def left_balance(T):
    left_child = T._left
    # left_child的左子树高。LL情况
    if left_child._bf == LH:
        # 做LL操作。旋转后左右子树应是等高的
        left_child._bf = EH
        T._bf = EH
        R_route(T)
    # left_child右子树的高度大。LR情况
    elif left_child._bf == RH:
        # 先更改各子树的bf
        left_child_right_child = left_child._right
        if left_child_right_child._bf == LH:
            T._bf = RH
            left_child._bf = EH
        elif left_child_right_child == EH:
            T._bf = EH
            left_child._bf = EH
        else:
            T._bf = EH
            left_child._bf = LH
        # 做LR操作
        left_child_right_child._bf = EH
        L_route(left_child)
        R_route(T)

# 右子树平衡化算法(类比于左子树平衡化操作)
def right_balance(T):
    pass

# 向AVL树中插入节点：构造平衡二叉查找树
is_taller = False # 全局变量，标志树是否长高
def insert_AVLTree(T, key):
    global is_taller
    # AVL树为空时
    if T is None:
        T = TreeNode(key, EH)
        is_taller = True
        return 0
    else:
        # 已有的关键字不会插入到AVl树中
        if T._data == key:
            return 0
        if T._data > key: # 插入左子树中
            if insert_AVLTree(T._left, key) == 0: # 插入不成功
                return 0
            if is_taller is True: # 判断如果长高
                if T._bf == LH: # 原本左子树高（现在又长高了，说明左子树比右子树高2，打破了平衡，需要做左子树平衡化操作）
                    left_balance(T)
                    is_taller = False
                elif T._bf == EH: # 原来左右子树等高
                    T._bf = LH # 现在左子树高
                    is_taller = True
                else: # 原来右子树高，现在树等高
                    T._bf = EH
                    is_taller = False
        else: # 插入右子树中
            if insert_AVLTree(T._right, key) == 0: # 插入不成功
                return 0
            if is_taller is True: # 判断是否长高
                if T._bf == LH:
                    T._bf = EH
                    is_taller = False
                elif T._bf == EH:
                    T._bf = RH
                    is_taller = True
                else:
                    right_balance(T)
                    is_taller = False

    return 1




