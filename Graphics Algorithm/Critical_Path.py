# encoding=utf-8
# date:2016-10-04
# gaooz.com
# 关键路径算法

MIN = -9999
MAX = 9999
# 有向无环网定义
class GraphicsNode(object):
    def __init__(self, data, neighbors = None):
        '''
        in_degree表示该顶点的入度
        '''
        self._data = data
        self._in_degree = 0
        self._neighbors = neighbors

# 关键路径
def critical_path(graphics):
    result = topo_sort_order(graphics)
    if result is False:
        return
    topo_order = result[0]
    ve = result[1]
    # 存放各个顶点最晚开始时间
    vl = []
    for i in range(len(graphics)):
        vl.append(MAX)
    # 按逆拓扑排序求每个顶点的最晚开始时间
    for  i in range(len(topo_order)-2, 0, -1):
        for j in range(len(graphics[i]._neighbors)):
            if ve[graphics[i]._neighbors[j][0]] - \
                    graphics[i]._neighbors[j][1] < vl[i]:
                vl[i] = ve[graphics[i]._neighbors[j][0]] - \
                        graphics[i]._neighbors[j][1]

    print "critical path:",graphics[0]._data,
    for i in range(1, len(graphics)-1):
        if ve[i] == vl[i]:
            print graphics[i]._data,
    print graphics[len(graphics)-1]._data



# 利用拓扑排序计算该有向无环网的拓扑序列并计算每个顶点的最早开始时间
def topo_sort_order(graphics):
    # 计算节点如度
    count_indegree(graphics)
    # 存放拓扑排序序列
    topo_order = []
    # 存放对应的每个顶点的最早开始时间
    ve = []
    for i in range(len(graphics)):
        ve.append(MIN) # 初始化为最小
    # 存放入度为0的顶点
    s = []

    #　在AOV网中第一个入度为0的点一定是源点
    start_index = find_indegree_zero(graphics)
    s.append(start_index)
    # 源点的最早开始时间
    ve[start_index] = 0
    while len(s) != 0:
        index = s.pop(len(s)-1)
        topo_order.append(index)
        if graphics[index]._neighbors is None:
            continue
        # 计算从index顶点出发的弧的弧头顶点的最早开始时间
        for i in range(len(graphics[index]._neighbors)):
            if ve[graphics[index]._neighbors[i][0]] < ve[index] + \
                    graphics[index]._neighbors[i][1]:
                ve[graphics[index]._neighbors[i][0]] = ve[index] + \
                    graphics[index]._neighbors[i][1]
            # 去除该顶点后更改其邻接顶点的入度
            graphics[graphics[index]._neighbors[i][0]]._in_degree -= 1
            if graphics[graphics[index]._neighbors[i][0]]._in_degree == 0:
                s.append(graphics[index]._neighbors[i][0])
    if len(topo_order) < len(graphics):
        return False # 非有向无环图
    return (topo_order, ve)


# 计算有向无环网中每个顶点的入度
def count_indegree(graphics):
    for i in range(len(graphics)):
        if graphics[i]._neighbors is not None:
            for j in range(len(graphics[i]._neighbors)):
                graphics[graphics[i]._neighbors[j][0]]._in_degree += 1

# 找到入度为0的顶点
def find_indegree_zero(graphics):
    for i in range(len(graphics)):
        if graphics[i]._in_degree == 0:
            return i
    return None

''' test

if __name__ == "__main__":
    v1 = GraphicsNode("v1", [[1, 6], [2, 4], [3, 5]])
    v2 = GraphicsNode("v2", [[4, 1]])
    v3 = GraphicsNode("v3", [[4, 1]])
    v4 = GraphicsNode("v4", [[5, 2]])
    v5 = GraphicsNode("v5", [[6, 9], [7, 7]])
    v6 = GraphicsNode("v6", [[7, 4]])
    v7 = GraphicsNode("v7", [[8, 2]])
    v8 = GraphicsNode("v8", [[8, 4]])
    v9 = GraphicsNode("v9")

    graphics = [v1, v2, v3, v4, v5, v6, v7, v8, v9]
    critical_path(graphics)
'''