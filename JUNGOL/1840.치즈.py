# bfs로 풀어야겠당..
# 바깥을 한바퀴 돌아서 녹는 지점을 알아내서 Q 에넣자

from collections import deque
def find_and_melt():
    cheese = []
    visit = [[0] * M for _ in range(N)]
    cnt = 0
    queue = deque([[0, 0], [0, M], [N,0], [N, M]])
    while queue:
        r, c = queue.popleft()
        for dr, dc in [(0, 1),(0, -1), (1, 0), (-1, 0)]:
            nr = r + dr
            nc = c + dc
            if nr < 0 or nc < 0 or nr >= N or nc >= M or visit[nr][nc]: continue
            if arr[nr][nc]:
                cheese.append([nr, nc])
                cnt += 1
            else:
                queue.append([nr,nc])
            visit[nr][nc] = 1

    # melt
    for r, c in cheese:
        arr[r][c] = 0
    if cnt :
        time_cnt.append(cnt)
        return True
    return False


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

time_cnt = []

while find_and_melt():
    find_and_melt()

hour =len(time_cnt)
print(hour)
if hour:
    print(time_cnt[-1])
else:
    print(0)