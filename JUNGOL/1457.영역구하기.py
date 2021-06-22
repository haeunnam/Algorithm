# 몇개의 영역 + 각 영역의 넓이
from collections import deque

def bfs(r, c):
    Q = deque([[r, c]])
    area = 1
    arr[r][c] = 1
    while Q:
        r, c = Q.popleft()
        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nr = r + dr
            nc = c + dc
            if nr < 0 or nc < 0 or nr >= M or nc >= N or arr[nr][nc]: continue
            area += 1
            arr[nr][nc] = 1
            Q.append((nr, nc))

    return area

M, N, K = map(int, input().split())
arr = [[0] * N for _ in range(M)]

for _ in range(K):
    sc, sr, ec, er = map(int, input().split())
    for r in range(sr, er):
        for c in range(sc, ec):
            arr[r][c] = 1

areas = []
for i in range(M):
    for j in range(N):
        if not arr[i][j]:
            areas.append(bfs(i, j))

print(len(areas))
print(*sorted(areas))
