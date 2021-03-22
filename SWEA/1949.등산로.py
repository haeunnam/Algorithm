
delta = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def DFS(r, c, cnt, K_used):
    global max_length
    visited[r][c] = 1
    for dt in range(4):
        nr = r + delta[dt][0]
        nc = c + delta[dt][1]
        if 0 > nr or nr >= N or 0 > nc or nc >= N or visited[nr][nc] == 1: continue
        # 이전 등산로보다 낮을 경우
        if map_info[nr][nc] < map_info[r][c]:
            visited[nr][nc] = 1
            DFS(nr, nc, cnt + 1, K_used)
            visited[nr][nc] = 0
        # 허용 깊이까지 깎을 수 있고, 아직 깎아본적 없을때
        elif map_info[nr][nc] - K < map_info[r][c] and K_used == 0:
            temp = map_info[nr][nc]
            map_info[nr][nc] = map_info[r][c] - 1
            K_used = 1
            visited[nr][nc] = 1
            DFS(nr, nc, cnt + 1, K_used)
            K_used = 0
            visited[nr][nc] = 0
            map_info[nr][nc] = temp
    else:
        if max_length < cnt:
            max_length = cnt

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    map_info = []
    for i in range(N):
        map_info.append(list(map(int, input().split())))


    # 가장 높은 봉우리 찾고 좌표 저장
    start = []
    max_peak = 0
    for i in range(N):
        for j in range(N):
            if map_info[i][j] < max_peak: continue
            if map_info[i][j] > max_peak:
                start = []
            max_peak = map_info[i][j]
            start.append((i, j))

    max_length = 0
    for i in range(len(start)):
        sr, sc = start[i][0], start[i][1]
        visited = [[0] * N for _ in range(N)]
        DFS(sr, sc, 1, 0)
    print(f'#{tc} {max_length}')


