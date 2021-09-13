from collections import deque


def solution(n, computers):
    answer = 0
    visited = [0] * n

    # queue 돌려서 방문표시하고 네트워크마다 cnt += 1
    def bfs(a):
        Q = deque([a])
        visited[a] = 1
        while Q:
            r = Q.popleft()
            for nc in range(n):
                if computers[r][nc] == 0 or r == nc or visited[nc]: continue
                visited[nc] = 1
                Q.append(nc)
        return

    cnt = 0
    # 네트워크 찾기
    for i in range(n):
        for j in range(n):
            if computers[i][j] == 1 and visited[i] == 0:
                bfs(i)
                cnt += 1
    return answer

solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]])