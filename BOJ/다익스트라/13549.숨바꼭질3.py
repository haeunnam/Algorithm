
from collections import deque

def find_K():
    D = [0xfffffffffff] * 100001
    D[N] = 0
    Q = deque()
    Q.append((0, N))
    while Q:
        time, loc = Q.popleft()
        if D[K] <= time: continue
        for n_time, n_loc in [(time+1, loc+1), (time+1, loc-1), (time, loc*2)]:
            if 0 > n_loc or 100000 < n_loc: continue
            if D[n_loc] > n_time:
                D[n_loc] = n_time
                Q.append((n_time, n_loc))

    return D[K]


N, K = map(int, input().split()) # 수빈, 동생
# 순간이동은 0초 , +1, -1 은 1초
print(find_K())