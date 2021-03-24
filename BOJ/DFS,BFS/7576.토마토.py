from collections import deque

delta = [(1, 0), (-1, 0), (0, 1), (0, -1)]

M, N = map(int, input().split())
box = []
for i in range(N):
    box.append(list(map(int, input().split())))

# 익은 토마토 구하기
Q = deque()
for i in range(N):
    for j in range(M):
        if box[i][j] == 1:
            Q.append((i, j))

while Q:
    r, c = Q.popleft()
    for dt in range(4):
        nr = r + delta[dt][0]
        nc = c + delta[dt][1]
        if 0 <= nr < N and 0 <= nc < M:
            if box[nr][nc] == 0:
                box[nr][nc] = box[r][c] + 1
                Q.append((nr, nc))
    if len(Q) == 0:
        ans = box[r][c]-1

for i in range(N):
    for j in range(M):
        if box[i][j] == 0:
            ans = -1

print(ans)







