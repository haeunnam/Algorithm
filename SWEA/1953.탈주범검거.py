from collections import deque

delta = [(-1, 0), (0, -1), (1, 0), (0, 1)]

T = int(input())
# 세로 크기 N, 가로 크기 M, 맨홀 뚜껑이 위치한장소의 세로 위치 R, 가로 위치 C, 그리고 탈출 후 소요된 시간 L
for tc in range(1, T+1):
    N, M, R, C, L = map(int, input().split())
    tunnel = [input().split() for _ in range(N)]
    pipe = [[], [0, 1, 2, 3], [0, 2], [1, 3], [0, 3], [2, 3], [1, 2], [0, 1]]
    Q = deque()

    # 맨홀부터 시작해서 갈수 있는곳 계속 방문체크하기
    manhole = (R, C)
    visited = [[0]*M for _ in range(N)]
    Q.append(manhole)
    visited[R][C] = 1

    # 시간 계산하기, visited 방문횟수 세기
    # 파이프 연결되어있는지 확인하고 가야함
    ans = 1
    time = 1
    while Q:
        if time == L : break
        size = len(Q)
        time += 1
        for i in range(size):
            r, c = Q.popleft()
            pipe_shape = int(tunnel[r][c])
            # 파이프 방향 찾기
            for direction in pipe[pipe_shape]:
                nr = r + delta[direction][0]
                nc = c + delta[direction][1]
                if 0 <= nr < N and 0 <= nc < M and visited[nr][nc] == 0:
                    n_direction = (direction + 2) % 4
                    if n_direction in pipe[int(tunnel[nr][nc])]:
                        visited[nr][nc] = visited[r][c] + 1
                        Q.append((nr, nc))
                        ans += 1


    print(f'#{tc} {ans}')

############ 다른 풀이


from collections import deque

delta = [(-1, 0), (0, -1), (1, 0), (0, 1)]
pipe = [[], [0, 1, 2, 3], [0, 2], [1, 3], [0, 3], [2, 3], [1, 2], [0, 1]]


T = int(input())
# 세로 크기 N, 가로 크기 M, 맨홀 뚜껑이 위치한장소의 세로 위치 R, 가로 위치 C, 그리고 탈출 후 소요된 시간 L
for tc in range(1, T+1):
    N, M, R, C, L = map(int, input().split())
    tunnel = [list(map(int, input().split())) for _ in range(N)]
    Q = deque()

    visited = [[0]*M for _ in range(N)]
    Q.append((R, C))
    visited[R][C] = 1
    position = [0] * (L+1) # 시간대별 가능 위치 수


    while Q:
        r, c = Q.popleft()
        position[visited[r][c]] += 1 # 시간대에 도착하는 칸번호
        if visited[r][c] < L:
            for dir in pipe[tunnel[r][c]]:
                nr = r + delta[dir][0]
                nc = c + delta[dir][1]
                if 0 <= nr < N and 0 <= nc < M and visited[nr][nc] == 0:
                    if (dir + 2) % 4 in pipe[tunnel[nr][nc]]:
                        visited[nr][nc] = visited[r][c] + 1
                        Q.append((nr, nc))


    print(f'#{tc} {sum(position)}')







