from collections import deque

delta = [(0, 1), (0, -1), (1, 0), (-1, 0)]
for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    way = [list(input()) for _ in range(N)]
    Q = deque()
    visit = [[-1] * M for _ in range(N)]
    ans = 0

    # W 좌표 찾기
    for i in range(N):
        for j in range(M):
            if way[i][j] == 'W':
                Q.append((i, j))
                visit[i][j] = 0

    while Q:
        r, c = Q.popleft()
        for dt in range(4):
            nr = r + delta[dt][0]
            nc = c + delta[dt][1]
            if nr < 0 or nr >= N or nc < 0 or nc >= M: continue
            if visit[nr][nc] != -1: continue
            Q.append((nr, nc))
            visit[nr][nc] = visit[r][c] + 1
            ans += visit[nr][nc]

    print("#{} {}".format(tc, ans))