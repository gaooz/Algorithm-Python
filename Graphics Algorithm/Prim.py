# encoding=utf-8
# date:2016-10-04
# gaooz.com
# Prim算法：求解加权连通图的最小生成树

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

# prim算法
def prim(graphics):
    if graphics is None or len(graphics) == 0:
        return None
    # 随机找到第一个顶点加入到最小生成树中
    # 标记该节点已经找到了
    graphics[0]._flag = True
    # 记录已经找到的节点个数
    count = 1
    # 以这个节点利用贪心算法不断将节点加入到最小生成树列表中
    # 直到所有节点都已加入到列表中为止
    while count != len(graphics):
        # 遍历图中已经找到的节点，从这些节点出发找到一条最小的边
        # 要求：边的另一个节点是还未找到的节点
        node = None # 记录节点
        edge = 0 # 记录最小的边
        weight = 9999 # 记录边上的权值，初始化为最大
        for i in range(len(graphics)):
            if graphics[i]._flag is True:
                for j in range(len(graphics[i]._neighbors)):
                    # 说明该节点的该条边的另一个顶点还未加入到已找到的列表节点中
                    if graphics[i]._neighbors[j][0]._flag is False and \
                            graphics[i]._neighbors[j][2] is False and \
                                    graphics[i]._neighbors[j][1] < weight:
                        node = graphics[i]
                        edge = j
                        weight = node._neighbors[edge][1]
        node._neighbors[edge][0]._flag = True
        node._neighbors[edge][2] = True
        count += 1

''' test

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

    prim(graphics)

    for i in range(len(graphics)):
        for j in range(len(graphics[i]._neighbors)):
            if graphics[i]._neighbors[j][2] is True:
                print graphics[i]._data + "-" + graphics[i]._neighbors[j][0]._data, \
                      graphics[i]._neighbors[j][1]
'''
