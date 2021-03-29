
# 이진탐색으로 해서 시간 단축

def binary_search(s, e):
    while True:
        mid = (s + e)// 2
        if (mid ** 2) == N:
            return mid
        elif mid ** 2> N:
            e = mid
        else:
            s = mid

N = int(input())
print(binary_search(1, N))
