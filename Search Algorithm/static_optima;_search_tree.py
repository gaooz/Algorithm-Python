# encoding=utf-8
# date:2016-09-26
# gaooz.com
# 静态次优查找树：适用于有序序列中元素查找概率不等的情景

class TreeNode(object):
    def __init__(self, data, left = None, right = None):
        self._data = data
        self._left = left
        self._right = right

# 构造静态次优查找树
# arr: 有序序列
# weight：有序序列中对应的每个元素的权重，权重越大查找的概率越高
def static_optimal_search_tree(arr, weight, low, high):
    if low > high:
        return None
    # 计算得到累加权重sw
    sw = []
    for i in range(low, high+1):
        if i == low:
            sw.append(weight[i])
        else:
            sw.append(sw[(i-1)-low]+weight[i])
    # 计算得到p
    p = []
    for i in range(low, high+1):
        if i == low:
            p.append(abs(sw[len(sw)-1]-sw[i-low]))
        else:
            p.append(abs(sw[len(sw)-1]-sw[i-low]-sw[i-1-low]))
    # 选择最小的p值为根节点
    min = 0
    for i in range(len(p)):
        if p[i] < p[min]:
            min = i
    min = min + low
    # 构造树根节点
    return TreeNode(arr[min], static_optimal_search_tree(arr, weight, low, min-1)\
                    , static_optimal_search_tree(arr, weight, min+1, high))

''' test

if __name__ == "__main__":
    arr = ["A", "B", "C", "D", "E", "F", "G", "H", "I"]
    weight = [1, 1, 2, 5, 3, 4, 4, 3, 5]
    root = static_optimal_search_tree(arr, weight, 0 ,8)
    print root._data

'''


