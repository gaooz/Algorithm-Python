# encoding=utf-8
# date:2016-10-03
# gaooz.com
# 广度优先遍历

# 图节点的定义
class GraphicsNode(object):
    def __init__(self, data, neighbors = None):
        self._data = data
        # 图中与该顶点有关系的顶点集合
        self._neighbors = neighbors

# 用队列实现广度优先搜索遍历
def BFSTraverse(graphics):
    # 初始化所有的顶点为未访问的状态
    for i in range(len(graphics)):
        graphics[i]._isTraverse = False
    # 队列
    queue = []
    for i in range(len(graphics)):
        if graphics[i]._isTraverse is False:
            graphics[i]._isTraverse = True
            print graphics[i]._data
            queue.append(graphics[i])
            while len(queue) != 0:
                node = queue.pop(0) # 队首元素出队
                # 访问该顶点的邻接顶点并依次将他们入队
                for j in range(len(node._neighbors)):
                    if node._neighbors[j]._isTraverse is False:
                        node._neighbors[j]._isTraverse = True
                        print node._neighbors[j]._data
                        queue.append(node._neighbors[j])
''' test
if __name__ == "__main__":
    node1 = GraphicsNode(1, [])
    node2 = GraphicsNode(2, [])
    node3 = GraphicsNode(3, [])
    node4 = GraphicsNode(4, [])
    node5 = GraphicsNode(5, [])

    node1._neighbors = [node2, node3]
    node2._neighbors = [node1, node4, node5]
    node3._neighbors = [node1, node5]
    node4._neighbors = [node2]
    node5._neighbors = [node2, node3]

    graphics = [node1, node2, node3, node4, node5]
    BFSTraverse(graphics)
'''