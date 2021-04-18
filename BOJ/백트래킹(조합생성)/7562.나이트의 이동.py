

dr = [-2, -1, 1, 2, 2, 1, -1, -2]
dc = [1, 2, 2, 1, -1, -2, -2, -1]

from collections import deque
def go(sr, sc):
    Q = deque()
    Q.append((sr, sc))
    moved = 0
    while Q:
        size = len(Q)
        for i in range(size):
            r, c = Q.popleft()
            if r >= N or c >= N: continue
            if r == er and c == ec:
                print(moved)
                return
            for dir in range(8):
                nr = r + dr[dir]
                nc = c + dc[dir]
                if nr < 0 or nc < 0 or nr >= N or nc >= N or visited[nr][nc]: continue
                visited[nr][nc] = 1
                Q.append((nr, nc))
        moved += 1
    return moved

# 몇번만에 도착하는지
for tc in range(1, int(input())+1):
    N = int(input()) # 체스판 한변의 길이
    sr, sc = map(int, input().split()) # 현재
    er, ec = map(int, input().split()) # 도착할 곳
    visited = [[0] * N for _ in range(N)]
    go(sr, sc)