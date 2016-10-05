# encoding=utf-8
# date:2016-10-04
# gaooz.com
# Dijkstra算法：单源最短路径算法

MAX = 9999

# 用邻接表结构存储网
# 弧、边定义
class GraphicsEdge(object):
    def __init__(self, data, index):
        self._data = data # 弧或边的权重
        self._index = index # 弧或边所依附的一个顶点下标，另一个顶点是拥有该弧的那个顶点

# 顶点定义
class GraphicsNode(object):
    def __init__(self, data, edges = None):
        self._data = data # 顶点的值
        self._edges = edges # 顶点所拥有的所有弧或边

# Dijkstra：单源最短路径算法
def dijkstra(graphics, index):
    '''
    求解网中第index个节点到其余各个节点的最短路径。
    返回一个最短路径列表。
    '''
    # 存放最短路径
    path = []
    # 存放最短路径长度
    dist = []

    # 初始化dist
    for i in range(len(graphics)):
        if i == index:
            dist.append(0)
        else:
            dist.append(MAX)
            j = 0
            while j < len(graphics[index]._edges):
                if i == graphics[index]._edges[j]._index:
                    dist.pop(len(dist)-1)
                    dist.append(graphics[index]._edges[j]._data)
                    break
                j += 1

    # 标记节点是否找到了最短路径
    flag = []
    # 初始化flag和path
    for i in range(len(graphics)):
        flag.append(False)
        path.append([])

    # 标记第index个节点已找到最短路径既是0
    flag[index] = True
    path[index].append(graphics[index]._data)

    # 找到剩余n-1个节点的最短路径
    count = 1
    old_min_index = index
    min_index = old_min_index
    min_weight = MAX
    while count < len(graphics):
        min_index = None
        min_weight = MAX
        for i in range(len(graphics)):
            if flag[i] is False and min_weight > dist[i]:
                min_weight = dist[i]
                min_index = i
        # 保存路径
        if min_index is None:
            break
        for i in range(len(path[old_min_index])):
            path[min_index].append(path[old_min_index][i])
        path[min_index].append(graphics[min_index]._data)
        # 标记为已经找到最短路径
        flag[min_index] = True

        # 更改路径值
        for i in range(len(dist)):
            if flag[i] is False:
                k = None
                for m in range(len(graphics[min_index]._edges)):
                    if graphics[min_index]._edges[m]._index == i:
                        k = m
                        break
                # 更新dist中的路径值
                if k is not None and \
                        graphics[min_index]._edges[k]._data + dist[min_index] < \
                        dist[i]:
                    dist[i] = graphics[min_index]._edges[k]._data + dist[min_index]
                    old_min_index = min_index
        count += 1

    return (dist, path)

''' test

if __name__ == "__main__":
    A = GraphicsNode("A", [GraphicsEdge(6, 1), GraphicsEdge(3, 2)])
    B = GraphicsNode("B", [GraphicsEdge(6, 0), GraphicsEdge(2, 2), GraphicsEdge(5, 3)])
    C = GraphicsNode("C", [GraphicsEdge(3, 0), GraphicsEdge(2, 1), GraphicsEdge(3, 3), \
                           GraphicsEdge(4, 4)])
    D = GraphicsNode("D", [GraphicsEdge(5, 1), GraphicsEdge(3, 2), GraphicsEdge(2, 4), \
                           GraphicsEdge(3, 5)])
    E = GraphicsNode("E", [GraphicsEdge(4, 2), GraphicsEdge(2, 3), GraphicsEdge(5, 5)])
    F = GraphicsNode("F", [GraphicsEdge(3, 3), GraphicsEdge(5, 4)])

    graphics = [A, B, C, D, E, F]

    result = dijkstra(graphics, 0)

    print "dist: ", result[0]
    print "path: ", result[1]
'''





