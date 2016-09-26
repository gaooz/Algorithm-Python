# encoding=utf-8
# date:2016-09-26
# gaooz.com
# 斐波那契查找

# 返回第n个斐波那契数
def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)

# 斐波那契查找：找到与有序序列arr的长度最接近的那个斐波那契数
# 然后，比较这个斐波那契数f对应位置的值是否是要查找的值，如果是则返回arr[f]
# 如果要查找的值比这个斐波那契数小，则在arr[0:f-1]这个范围内查找
# 如果要查找的值比这个斐波那契数大，则在arr[f+1:len(arr)-1]这个范围内查找
# 查找时下一个要比较的值是比这个斐波那契数小的或大的那个斐波那契数对应位置的值
# 最理想的情况是：有序序列的长度比某个斐波那契数小1，或正好等于某个斐波那契数

def fibonacci_search(arr, k, low, high):
    if low > high:
        return -1
    # 找到首个比该有序序列长度大的斐波那契数的位置
    fi_index = 0
    while True:
        if fibonacci(fi_index) > high-low:
            break
        fi_index = fi_index + 1

    # 从第fi_index-1个斐波那契数对应的位置开始查找
    index = fibonacci(fi_index-1)
    if arr[index] == k:
        return index
    if arr[index] < k:
        return fibonacci_search(arr, k, index+1, high)
    else:
        return fibonacci_search(arr, k, low, index-1)

''' test

if __name__ == "__main__":
    arr = [1,2,3,4,5,6]
    print fibonacci_search(arr, 6, 0, 5)

'''
