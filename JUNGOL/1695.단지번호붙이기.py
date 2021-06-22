from collections import deque


def bfs(r, c):
    Q = deque([[r, c]])
    arr[r][c] = '0'
    house_cnt = 1
    while Q:
        r, c = Q.popleft()
        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nr = r + dr
            nc = c + dc
            if nr < 0 or nc < 0 or nr >= N or nc >= N or arr[nr][nc] == '0': continue
            house_cnt += 1
            arr[nr][nc] = '0'
            Q.append((nr, nc))
    return house_cnt


N = int(input())
arr = [ list(input()) for i in range(N)]
danjies = []
for i in range(N):
    for j in range(N):
        if arr[i][j]=='1':
            danjies.append(bfs(i, j))
print(len(danjies))
for danji in sorted(danjies):
    print(danji)