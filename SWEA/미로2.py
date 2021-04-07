from collections import deque

delta = [(-1, 0),(0, -1) ,(0, 1), (1, 0)]

def bfs():
    Q = deque()
    Q.append((sr, sc))
    while Q:
        r, c = Q.popleft()
        for dt in range(4):
            nr = r + delta[dt][0]
            nc = c + delta[dt][1]
            if 0 <= nr < N and 0 <= nc < N:
                if arr[nr][nc] == 0:
                    arr[nr][nc] = 1
                    Q.append((nr, nc))
                else:
                    if arr[nr][nc] == 2:
                        return 1
    return 0


for _ in range(10):
    tc = int(input())
    arr = []
    N = 100
    for i in range(N):
        arr.append(list(map(int, input())))

    for i in range(N):
        for j in range(N):
            if arr[i][j] == 3:
                sr, sc = i, j
                break

    print(f'#{tc} {bfs()}')