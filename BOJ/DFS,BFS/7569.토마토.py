from collections import deque


def find_riped_tomatoes():
    for floor in range(H):  # 층수
        for i in range(N):  # ROW값
            for j in range(M):  # COL값
                # 익은 토마토 찾기
                if tomatoes[floor][i][j] == 1:
                    Q.append((floor, i, j))

    return

def make_tomatoes_riped():
    cnt = -1
    while Q:
        cnt += 1
        size = len(Q)
        for i in range(size):
            f, r, c = Q.popleft()
            for dt in range(6):
                nf = f + delta[dt][0]
                nr = r + delta[dt][1]
                nc = c + delta[dt][2]
                if 0 <= nr < N and 0 <= nc < M and 0 <= nf < H:
                    if tomatoes[nf][nr][nc] == 0:
                        tomatoes[nf][nr][nc] = 1
                        Q.append((nf, nr, nc))
    return cnt

# 아직도 안익은 토마토 찾기
def check_toamtes(ans):
    for floor in range(H):  # 층수
        for i in range(N):  # ROW값
            for j in range(M):  # COL값
                if tomatoes[floor][i][j] == 0:
                    return -1
    return ans

delta = [(0, 1, 0), (0, 0, 1), (0, 0, -1), (0, -1, 0),(1, 0, 0), (-1, 0, 0)]
M, N, H = map(int, input().split())
tomatoes = []
Q = deque()

# 토마토 값 저장
for i in range(H):
    box = []
    for j in range(N):
        box.append(list(map(int, input().split())))
    tomatoes.append(box)

find_riped_tomatoes()
ans = check_toamtes(make_tomatoes_riped())

print(ans)


