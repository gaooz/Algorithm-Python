# encoding=utf-8
# date:2016-10-03
# gaooz.com
# 拓扑排序

'''
拓扑排序适用于有向无环图，可以用该算法判断有向图是否存在环路
'''

# 图节点的定义
class GraphicsNode(object):
    def __init__(self, data, neighbors = None):
        self._data = data
        # 图中与该顶点有关系的顶点集合
        self._neighbors = neighbors

# 计算图中各个顶点的入度
def count_indegree(graphics):
    for i in range(len(graphics)):
        try:
            graphics[i]._indegree += 1
        except:
            graphics[i]._indegree = 0
        else:
            graphics[i]._indegree -= 1
        if graphics[i]._neighbors is not None:
            for j in range(len(graphics[i]._neighbors)):
                try:
                    graphics[i]._neighbors[j]._indegree += 1
                except:
                    graphics[i]._neighbors[j]._indegree = 0

# 找到入度为0的顶点
def find_indegree_iszero(graphics):
    for i in range(len(graphics)):
        if graphics[i]._indegree == 0:
            return i
    return -1

# 拓扑排序
def toposort(graphics):
    # 拓扑序列
    topo_list = []
    count_indegree(graphics)
    node_index = find_indegree_iszero(graphics)
    if node_index == -1:
        return None

    while len(graphics) != 0 and node_index != -1:
        # 从图中移除该顶点和以该顶点为尾的弧
        node = graphics.pop(node_index)
        if node._neighbors is not None:
            for i in range(len(node._neighbors)):
                node._neighbors[i]._indegree -= 1
        # 重新计算各顶点的入度
        count_indegree(graphics)
        topo_list.append(node)
        node_index = find_indegree_iszero(graphics)

    if len(graphics) == 0:
        return topo_list
    return None

''' test

if __name__ == "__main__":
    node1 = GraphicsNode(1)
    node2 = GraphicsNode(2)
    node3 = GraphicsNode(3)

    node1._neighbors = [node2, node3]
    graphics = [node1, node2, node3]
    result = toposort(graphics)
    if result is not None:
        for i in range(len(result)):
            print result[i]._data
'''



