
from collections import deque
delta = [(0, 1), (0, -1), (1, 0), (-1, 0)]

# 각 섬 시작점 찾기
def start_point(i, j, island):
    lst = set()
    Q = deque()
    Q.append((i, j))
    arr[i][j] = island
    while Q:
        r, c = Q.popleft()
        for dt in range(4):
            nr = r + delta[dt][0]
            nc = c + delta[dt][1]
            if 0 > nr or nr >= N or 0 > nc or nc >= N : continue
            # 다음에 갈 방향 정하기
            if arr[nr][nc] == '1':
                Q.append((nr, nc))
                arr[nr][nc] = island
            # 시작점 좌표 정하기
            elif arr[nr][nc] == '0':
                lst.add((r, c))
                arr[r][c] = island
    starts.append(list(lst))
    return


# 좌표에서 출발해서 상대편 만나면, stop 하기
def bridge(island):
    global min_bridge
    visited = [[0] * N for i in range(N)]
    for i in range(N):
        for j in range(N):
            if arr[i][j] == island+1:
                visited[i][j] = arr[i][j]
    cnt = 0
    Q = deque()
    Q.extend(starts[island])
    while Q:
        size = len(Q)
        cnt += 1
        if cnt > min_bridge:
            return
        # 본인이랑, '0'이 아닌 거 만나면 스탑하기
        for i in range(size):
            r, c = Q.popleft()
            for dt in range(4):
                nr = r + delta[dt][0]
                nc = c + delta[dt][1]
                if 0 > nr or nr >= N or 0 > nc or nc >= N or visited[nr][nc] or arr[nr][nc] == island: continue
                if arr[nr][nc] == '0': # 방문하지 않고, 바다이면
                    visited[nr][nc] = -1
                    Q.append((nr, nc))
                elif arr[nr][nc]: #  다른 섬에 도달하면
                    if min_bridge > cnt:
                        min_bridge = cnt
                        return
    return


N = int(input())
arr = [input().split() for i in range(N)]
starts = []
min_bridge = 10001
island = 0

for i in range(N):
    for j in range(N):
        if arr[i][j] == '1':
            island += 1 # 섬 구분
            start_point(i, j, island)

for i in range(island-1):
    bridge(i)

print(min_bridge-1)

