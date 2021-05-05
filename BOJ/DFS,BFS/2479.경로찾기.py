
from collections import deque

def hamming():
    visited[s] = 1
    Q = deque()
    Q.append((s, str(s)))
    while Q:
        num, code = Q.popleft()
        if num == e : return code
        for i in range(1, N+1):
            cnt = 0
            if visited[i]: continue
            for j in range(K):
                if arr[num][j] != arr[i][j]:
                    cnt += 1
                if cnt > 1:
                    break
            if cnt == 1:
                visited[i] = 1
                Q.append((i, code + ' ' + str(i)))

    return -1



N, K = map(int, input().split())
arr = ['0']+[input() for _ in range(N)]
s, e = map(int, input().split())
visited = [0] * (N+1)
print(hamming())
