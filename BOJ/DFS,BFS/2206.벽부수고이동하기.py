from collections import deque


N, M = map(int, input().split())
map = [list(map(int, input())) for _ in range(N)]
visited = [[[0] * 2 for _ in range(M)] for _ in range(N)]
delta = [(1, 0), (0, 1), (0, -1), (-1, 0)]


Q = deque()
def BFS():
    ans = -1
    Q.append((0, 0, 0))
    visited[0][0][0] = 1
    while Q:
        r, c, crash = Q.popleft()
        if r == N-1 and c == M-1:
            ans = visited[N-1][M-1][crash]
            return ans
        for dt in range(4):
            nr = r + delta[dt][0]
            nc = c + delta[dt][1]
            if 0 <= nr < N and 0 <= nc < M:
                # 벽이 없고 방문하지 않았을때
                if map[nr][nc] == 0 and visited[nr][nc][crash] == 0 :
                    visited[nr][nc][crash] = visited[r][c][crash] + 1
                    Q.append((nr, nc, crash))
                # 벽이 있고, 아직 부수지 않았을 때
                elif map[nr][nc] == 1 and crash == 0:
                    visited[nr][nc][1] = visited[r][c][0] + 1
                    Q.append((nr, nc, 1))
    return ans

print(BFS())






