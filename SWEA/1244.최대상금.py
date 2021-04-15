import sys
sys.stdin =open('input.txt', 'r')
from collections import deque

def find_max(change):
    global ans
    val = int("".join(map(str, num)))
    Q = deque(val)
    while Q:
        for i in range(N-1):
            for j in range(i+1, N):
                num[i], num[j] = num[j], num[i]
                money(change-1)
                num[i], num[j] = num[j], num[i]
    return

for tc in range(1, int(input())+1):
    num, change = input().split()
    num = list(map(int, num))
    N = len(num)
    visited = [set() for _ in range(11)]
    change = int(change)
    ans = 0
    find_max(change)
    print('#{} {}'.format(tc,ans))
