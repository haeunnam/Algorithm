import sys
from collections import deque
delta = [(1, 0), (-1, 0), (0, 1), (0, -1)]
#

#불퍼지기
def fire():
    fr, fc = fQ.popleft()
    if fr - 1 >= 0 and arr[fr - 1][fc] == '.':
        fQ.append((fr - 1, fc))
        arr[fr - 1][fc] = '*'
    if fr + 1 < N and arr[fr + 1][fc] == '.':
        fQ.append((fr + 1, fc))
        arr[fr + 1][fc] = '*'
    if fc - 1 >= 0 and arr[fr][fc - 1] == '.':
        fQ.append((fr, fc - 1))
        arr[fr][fc - 1] = '*'
    if fc + 1 < M and arr[fr][fc + 1] == '.':
        fQ.append((fr, fc + 1))
        arr[fr][fc + 1] = '*'

def go_out():
    ans = 'IMPOSSIBLE'
    while Q:
        for _ in range(len(fQ)):
            fire()
        # 상근이 이동
        for _ in range(len(Q)):
            r, c = Q.popleft()
            if r == 0 or r == N-1 or c == 0 or c == M-1:
                ans = visited[r][c]
                return ans
            if r-1 >= 0 and arr[r-1][c] == '.' and visited[r-1][c] == 0:
                arr[r-1][c] == '@'
                visited[r-1][c] = visited[r][c] + 1
                Q.append((r-1, c))
            if r+1 < N and arr[r+1][c] == '.' and visited[r+1][c] == 0:
                arr[r+1][c] == '@'
                visited[r+1][c] = visited[r][c] + 1
                Q.append((r+1, c))
            if c-1 >= 0 and arr[r][c-1] == '.' and visited[r][c-1] == 0:
                arr[r][c-1] == '@'
                visited[r][c-1] = visited[r][c] + 1
                Q.append((r, c-1))
            if c+1 < M and arr[r][c+1] == '.' and visited[r][c+1] == 0:
                arr[r-1][c+1] == '@'
                visited[r][c+1] = visited[r][c] + 1
                Q.append((r, c+1))
    return ans


for tc in range(int(input())):
    M, N = map(int, input().split())
    arr = [list(input()) for _ in range(N)]
    visited = [[0]* M for _ in range(N)]
    Q = deque()
    fQ = deque()

    # 상근이 위치, 불 위치 찾기
    for i in range(N):
        for j in range(M):
            if arr[i][j] == '@':
                Q.append((i, j))
                visited[i][j] = 1
            if arr[i][j] == '*':
                fQ.append((i, j))

    print(go_out())