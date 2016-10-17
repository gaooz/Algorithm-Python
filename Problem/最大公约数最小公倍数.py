# encoding=utf-8
# gaooz.com
# 2016-10-17
# 最大公约数-最小公倍数


# 计算两个数的最大公约数
def greatest_common_factor(m, n):
    if m == n:
        return m
    if m > n:
        tmp = m
        m = n
        n = tmp
    for i in range(2, m+1):
        if m % i == 0 and n % i == 0:
            return i
    return 1

# 计算两个数的最小公倍数
def lowest_common_mutiple(m, n):
    if m == n:
        return m
    if m > n:
        tmp = m
        m = n
        n = tmp
    for i in range(m, m*n+1):
        if i % m ==0 and i % n == 0:
            return i


''' test

if __name__ == "__main__":
    print greatest_common_factor(2, 3)
    print lowest_common_mutiple(2, 3)

'''

