# 백준 7576과 동일 문제
from collections import deque
import sys
input = sys.stdin.readline

def make_ripe(start_tomatoes):
    queue = deque(start_tomatoes)
    while queue:
        r, c = queue.popleft()
        cur_days = box[r][c]
        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nr = dr + r
            nc = dc + c
            if nr < 0 or nr >= N or nc < 0 or nc >= M or box[nr][nc] != 0: continue
            box[nr][nc] = cur_days + 1
            queue.append((nr, nc))
    return cur_days

def still_unripe():
    for i in range(N):
        for j in range(M):
            if box[i][j] == 0 :
                return True
    return False

M, N = map(int, input().split())
box = []
for _ in range(N):
    box.append(list(map(int, input().split())))


# 익은 토마토 찾기
start = []
for i in range(N):
    for j in range(M):
        if box[i][j] == 1:
            start.append((i, j))

# 토마토 익히기(익힐 수 있는 경우만)
if start:
    ans = make_ripe(start) -1
# 모든 토마토가 익어있는 상태
else:
    ans = 0

# 토마토가 다 익지 않는 경우
if still_unripe():
    ans = -1

print(ans)