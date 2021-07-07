from collections import deque

def catch_target():
    queue = deque([(sr, sc, 0)])
    visited[sr][sc] = 1
    while queue:
        cr, cc, moved = queue.popleft()
        for dr, dc in move:
            nr = cr + dr
            nc = cc + dc
            # 범위 확인 정확히 (1~ N+1)
            if nr < 1 or nr > N or nc < 1 or nc > M: continue
            if visited[nr][nc]: continue
            if nr == er and nc == ec: return moved + 1
            visited[nr][nc] = 1
            queue.append((nr, nc, moved + 1))
    return moved

move = [(1, 2), (2, 1), (-1, -2), (-2, -1), (1, -2), (-2, 1), (2, -1), (-1, 2)]
N, M = map(int, input().split())
visited = [[0] * (M+1) for _ in range(N+1)]
sr, sc, er, ec = map(int, input().split())

print(catch_target())
