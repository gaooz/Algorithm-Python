# encoding=utf-8
# gaooz.com
# 2016-10-15
# 数组旋转

def reverse(arr, start_index, end_index):
    b = start_index 
    e = end_index

    while b < e:
        tmp = arr[e]
        arr[e] = arr[b]
        arr[b] = tmp
        b += 1
        e -= 1

def right_move():
    length = int(raw_input())
    arr = list(raw_input())
    k = int(raw_input())

    k %= length
    # 对arr的[0,length-k-1]进行翻转
    reverse(arr, 0, length-k-1)
    # 对arr的[length-k, length-1]进行翻转
    reverse(arr, length-k, length-1)
    # 对arr整体进行翻转
    reverse(arr, 0, length-1)

    for i in range(len(arr)):
        print arr[i],
    print

if __name__ == "__main__":
    right_move()