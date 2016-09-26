# encoding=utf-8
# date:2016-09-26
# gaooz.com
# KMP算法

# kmp算法
def kmp(base_str, sub_str):
    base_index = 0
    sub_index = 0
    # 得到next数组
    next = get_next(sub_str)

    while base_index < len(base_str) and sub_index < len(sub_str):
        if sub_str[sub_index] == base_str[base_index]:
            sub_index = sub_index + 1
            base_index = base_index + 1
        else:
            sub_index = next[sub_index]
            if sub_index == 0:
                base_index = base_index + 1
    if sub_index == len(sub_str):
        return base_index - len(sub_str)
    return -1

# 求取子串的next数组算法
def get_next(sub_str):
    index_i = 0
    index_j = -1
    # 初始化nextr数组
    next = []
    for i in range(len(sub_str)+1):
        next.append(0)

    while index_i < len(sub_str)-1:
        if index_j == -1 or sub_str[index_i] == sub_str[index_j]:
            index_i = index_i + 1
            index_j = index_j + 1
            if sub_str[index_i] != sub_str[index_j]:
                next[index_i] = index_j
            else:
                next[index_i] = next[index_j]
        else:
            index_j = next[index_j]

    return next

''' test

if __name__ == "__main__":
    base_str = "abcabc"
    sub_str = "bp"
    print kmp(base_str, sub_str)

'''