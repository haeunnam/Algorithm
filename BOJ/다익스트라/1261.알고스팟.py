
from collections import deque
INF = 0xfffffffffffffff

def solve():
    D = [[INF] * M for _ in range(N)]
    Q = deque()
    D[0][0] = 0
    Q.append((0, 0, 0))
    while Q:
        r, c, walls = Q.popleft()
        if D[r][c] < walls: continue
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nr = r + dr
            nc = c + dc
            if nr <0 or nr >= N or nc < 0 or nc >= M: continue
            # 벽이 뚤려있는 지 아닌지
            if maze[nr][nc] == '0' and D[nr][nc] > walls:
                D[nr][nc] = walls
                Q.append((nr, nc, walls))
            elif maze[nr][nc] == '1' and D[nr][nc] > walls + 1:
                D[nr][nc] = walls + 1
                Q.append((nr, nc, walls+1))
    return D[N-1][M-1]



M, N = map(int, input().split())
maze = []
for _ in range(N):
    maze.append(list(input()))

print(solve())