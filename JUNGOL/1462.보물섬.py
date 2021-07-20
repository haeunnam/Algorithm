# 백준 2589와 동일 문제
from collections import deque
import sys

input = sys.stdin.readline


def bfs(r, c):
    global distance
    visited = [[0] * M for _ in range(N)]
    queue = deque([(r, c)])
    visited[r][c] = 1
    while queue:
        cr, cc = queue.popleft()
        cur_visit = visited[cr][cc]
        if distance < cur_visit:
            distance = cur_visit
        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nr = cr + dr
            nc = cc + dc
            if nr < 0 or nr >= N or nc < 0 or nc >= M or visited[nr][nc]: continue
            if arr[nr][nc] == 'W': continue
            visited[nr][nc] = cur_visit + 1
            queue.append((nr, nc))
    return


N, M = map(int, input().split())
arr = []

for _ in range(N):
    arr.append(list(input()))
distance = 0
start = []

for i in range(N):
    for j in range(M):
        cnt = 0
        if arr[i][j] == "L":
            if i+1 < N and arr[i + 1][j] == 'L': cnt += 1
            if 0 <= i-1 and  arr[i - 1][j] == 'L': cnt += 1
            if j+1 < M and arr[i][j + 1] == 'L': cnt += 1
            if 0 <= j-1 and arr[i][j - 1] == 'L': cnt += 1
            if cnt < 3:
                start.append((i, j))
for r, c in start:
    bfs(r, c)


print(distance - 1)