# encoding=utf-8
# date:2016-09-25
# gaooz.com
# 链表逆置

# 定义链表节点
class LinkedNode(object):
    def __init__(self, data = None, next = None):
        self._data = data
        self._next = next

# 链表逆置
def reverse_linked_list(list_head):
    if list_head._next is None or list_head._next._next is None:
        return

    # 需要三个指针：
    # 头节点指针：list_head._next
    # 左边节点指针初始化：left=list_head._next
    # 右边节点指针初始化：right=list_head._next._next
    left = list_head._next
    right = list_head._next._next

    # 开始逆置
    while right is not None:
        if left is list_head._next:
            left._next = None
        else:
            left._next = list_head._next
        list_head._next = left
        left = right
        right = right._next
    # 最后一步
    left._next = list_head._next
    list_head._next = left

# 遍历单链表
def iterate_linked_list(list_head):
    if list_head is None or list_head._next is None:
        print "list is None"
        return
    p = list_head._next
    while p is not None:
        print p._data
        p = p._next

''' test

if __name__ == "__main__":
    list_head = LinkedNode(-1, None)
    p = LinkedNode(1, None)
    list_head._next = p
    k = LinkedNode(2, None)
    p._next = k

    iterate_linked_list(list_head)

    reverse_linked_list(list_head)

    iterate_linked_list(list_head)
'''





