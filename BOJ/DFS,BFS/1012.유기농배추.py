########모든 밭 돌아다니는 풀이
import sys

delta = [(0, 1), (0, -1), (1, 0), (-1, 0)]
for _ in range(int(input())):
    M, N, K =map(int, sys.stdin.readline().split())
    cabbage = [[0]* M for _ in range(N)]

    for _ in range(K):
        x, y = map(int, sys.stdin.readline().split())
        cabbage[y][x] = 1

    stack = []
    cnt = 0
    for i in range(N):
        for j in range(M):
            # 양배추 존재할때
            if cabbage[i][j]:
                cnt += 1
                cabbage[i][j] = 0
                stack.append((i, j))
            #인접한 곳 다 돌아다님
            while stack:
                r, c = stack.pop()
                for dt in range(4):
                    nr = r + delta[dt][0]
                    nc = c + delta[dt][1]
                    if 0 <= nr < N and 0 <= nc < M:
                        if cabbage[nr][nc]:
                            cabbage[nr][nc] = 0
                            stack.append((nr, nc))
    print(cnt)


######양배추 좌표값만 돌아다니는 풀이

delta = [(0, 1), (0, -1), (1, 0), (-1, 0)]
for _ in range(int(input())):
    M, N, K = map(int, input().split())
    cabbage = [[0]* M for _ in range(N)]

    need_to_visit = []
    for _ in range(K):
        x, y = map(int, input().split())
        cabbage[y][x] = 1
        # 방문해야할 곳 미리 표시
        need_to_visit.append((y,x))

    stack = []
    cnt = 0
    # 양배추 있는 곳들 돌아다님
    for k in range(K):
        i, j = need_to_visit[k]
        # 방문하지 않았으면 방문처리 cabbage 행렬을 방문처리로 이용
        if cabbage[i][j]:
            cnt += 1
            cabbage[i][j] = 0
            stack.append((i, j))
        while Q:
            r, c = stack.pop()
            for dt in range(4):
                nr = r + delta[dt][0]
                nc = c + delta[dt][1]
                if 0 <= nr < N and 0 <= nc < M:
                    if cabbage[nr][nc]:
                        cabbage[nr][nc] = 0
                        stack.append((nr, nc))
    print(cnt)