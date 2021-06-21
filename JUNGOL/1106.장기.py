from collections import deque
N, M = map(int, input().split())
r, c, s, k = map(int, input().split())
# r c 는 말, s k 는 졸
direction = {1: [-2, 1],
             2: [-1, 2],
             3: [1, 2],
             4:[2, 1],
             5: [2, -1],
             6: [1,-2],
             7:[-1,-2],
             8:[-2, -1]
             }

visited = [[0] * M for _ in range(N)]
visited[r-1][c-1] = 1
target_r, target_c = s-1, k-1
def catch():
    Q = deque([[r-1,c-1, 0]])
    while Q:
        cur_r, cur_c, cnt = Q.popleft()
        for d in range(1, 9):
            nr = cur_r + direction[d][0]
            nc = cur_c + direction[d][1]
            if nc < 0 or nc >= M or nr < 0 or nr >= N or visited[nr][nc]: continue
            if nr == target_r and nc == target_c: return cnt + 1
            visited[nr][nc] = 1
            Q.append([nr,nc,cnt+1])

print(catch())