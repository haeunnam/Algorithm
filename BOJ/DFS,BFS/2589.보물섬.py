
import sys
from collections import deque

n, m = map(int, (sys.stdin.readline().split()))
map = []
ans = 0
for _ in range(n):
    map.append(sys.stdin.readline())

start = []

# L과 인접해 있는 면이 2면이하 일때 시작점으로 넣음
for i in range(n):
    for j in range(m):
        cnt = 0
        if map[i][j] == "L":
            if i+1 < n and map[i + 1][j] == 'L': cnt += 1
            if 0 <= i-1 and  map[i - 1][j] == 'L': cnt += 1
            if j+1 < m and map[i][j + 1] == 'L': cnt += 1
            if 0 <= j-1 and map[i][j - 1] == 'L': cnt += 1
            if cnt < 3:
                start.append((i, j))



# BFS 이용하여 가장 먼 위치에서 최단 거리 찾아내기
Q = deque()
for k in range(len(start)):
    sr, sc = start[k][0], start[k][1]
    distance = [[-1] * m for _ in range(n)]
    Q.append((sr, sc))
    distance[sr][sc] = 0
    while Q:
        r, c = Q.popleft()
        if 0 <= r-1 and distance[r-1][c] == -1 and map[r-1][c] == 'L':
            Q.append((r-1, c))
            distance[r-1][c] = distance[r][c] + 1
        if r+1 < n and distance[r+1][c] == -1 and map[r+1][c] == 'L':
            Q.append((r+1, c))
            distance[r+1][c] = distance[r][c] + 1
        if 0 <= c-1 and distance[r][c-1] == -1 and map[r][c-1] == 'L':
            Q.append((r, c-1))
            distance[r][c-1] = distance[r][c] + 1
        if c+1 < m and distance[r][c+1] == -1 and map[r][c+1] == 'L':
                    Q.append((r, c+1))
                    distance[r][c+1] = distance[r][c] + 1
        if len(Q) == 0:
            if distance[r][c] > ans:
                ans = distance[r][c]

print(ans)
