from collections import deque

def kill():
    global max_sec
    queue = deque([(sr-1, sc-1, 3)])
    arr[sr - 1][sc - 1] = '0'
    while queue:
        cr, cc, sec = queue.popleft()
        if max_sec < sec:
            max_sec = sec
        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nr = dr + cr
            nc = dc + cc
            if nr < 0 or nr >= N or nc < 0 or nc >= M or arr[nr][nc] == '0': continue
            arr[nr][nc] = '0'
            queue.append((nr, nc, sec + 1))

    return

M, N = map(int, input().split())
arr = []
for _ in range(N):
    arr.append(list(input()))
sc, sr = map(int, input().split())
max_sec = 0
kill()


rest = 0
for i in range(N):
    for j in range(M):
        if arr[i][j] == '1':
            rest += 1

print(max_sec)
print(rest)
