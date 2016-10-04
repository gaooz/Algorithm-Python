# encoding=utf-8
# date:2016-10-04
# gaooz.com
# Kruskal算法：求解加权连通图的最小生成树

# 网中节点定义
class GraphicsNode(object):
    def __init__(self, data, neighbors = None):
        '''
        neighbors: 是一个列表，列表的元素是具有三个元素的列表类型。
        列表的第一个元素表示该节点的邻接点，第二个元素表示边的权值，第三个元素是该边的标记。
        '''
        self._data = data
        self._neighbors = neighbors
        # 顶点标记。比如：标记该顶点是否被遍历过或者是否加入了已找到的顶点集合中
        self._flag = False

# Kruskal算法：求解加权连通图的最小生成树
def kruskal(graphics):
    if graphics is None or len(graphics) == 0:
        return
    # 记录有多少条边已经找到了
    count = 0
    # n个顶点连通图的最小生成树有n-1条边
    while count != len(graphics)-1:
        # 寻找具有最小边的权重，初始化为最大
        weight = 9999
        node = None
        edge_index = 0
        # 遍历所有边找到当前还未加入到最小生成树中的最小权重边
        for i in range(len(graphics)):
            for j in range(len(graphics[i]._neighbors)):
                if graphics[i]._neighbors[j][2] is False and \
                        graphics[i]._neighbors[j][1] < weight:
                    node = graphics[i]
                    edge_index = j
                    weight = node._neighbors[edge_index][1]
        # 判断这条边所依附的两个顶点是否在同一个连通分量上
        # 如果在则抛弃这条边，否则将其加入。
        if is_connected(graphics, node, node._neighbors[edge_index][0]) is False:
            # 标记找到的边
            node._neighbors[edge_index][2] = True
            for k in range(len(node._neighbors[edge_index][0]._neighbors)):
                if node._neighbors[edge_index][0]._neighbors[k][0] is node:
                    node._neighbors[edge_index][0]._neighbors[k][2] = True
            count += 1
        else:
            # 抛弃这条边
            node._neighbors[edge_index][2] = "NO"

# 判断这两个顶点是否是在同一个连通分量上
def is_connected(graphics, v1, v2):
    # 初始化未被访问
    for i in range(len(graphics)):
        graphics[i]._flag = False
    # 从顶点v1开始深度优先遍历，如果能遍历到v顶点v2则说明v1、v2在一个连通分量上
    DFS(v1)
    return v2._flag

# 深度遍历，只沿着边的标记为True的边遍历
def DFS(node):
    node._flag = True
    for i in range(len(node._neighbors)):
        if node._neighbors[i][2] is True and node._neighbors[i][0]._flag is False:
            DFS(node._neighbors[i][0])
''' test

注意：无向网中相同两个顶点之间的边应该具有一条

if __name__ == "__main__":
    v1 = GraphicsNode("v1")
    v2 = GraphicsNode("v2")
    v3 = GraphicsNode("v3")
    v4 = GraphicsNode("v4")
    v5 = GraphicsNode("v5")
    v6 = GraphicsNode("v6")

    v1._neighbors = [[v2, 6, False], [v3, 1, False], [v4, 5, False]]
    v2._neighbors = [[v1, 6, False], [v3, 5, False], [v5, 3, False]]
    v3._neighbors = [[v1, 1, False], [v2, 5, False], [v4, 5, False], [v5, 6, False], [v6, 4, False]]
    v4._neighbors = [[v1, 5, False], [v3, 5, False], [v6, 2, False]]
    v5._neighbors = [[v2, 3, False], [v3, 6, False], [v6, 6, False]]
    v6._neighbors = [[v3, 4, False], [v4, 2, False], [v5, 6, False]]

    graphics = [v1, v2, v3, v4, v5, v6]

    kruskal(graphics)

    for i in range(len(graphics)):
        for j in range(len(graphics[i]._neighbors)):
            if graphics[i]._neighbors[j][2] is True:
                print graphics[i]._data + "-" + graphics[i]._neighbors[j][0]._data, \
                      graphics[i]._neighbors[j][1]
'''

