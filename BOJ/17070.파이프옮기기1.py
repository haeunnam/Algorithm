
### 재귀 pypy
def find_cases(r, c, dir):
    global cnt
    if r == N-1 and c == N-1:
        cnt += 1
        return

    if dir == 0 or dir == 2: # 가로로 가는 경우
        if c + 1 < N and arr[r][c+1] == 0:
            find_cases(r, c+1, 0)

    if dir == 1 or dir == 2: # 세로로 가는 경우
        if r + 1 < N and arr[r+1][c] == 0:
            find_cases(r+1, c, 1)

    # 대각선으로 가는 경우
    if c + 1 < N and r + 1 < N and arr[r+1][c+1] == 0:
        if arr[r][c+1] == 0 and arr[r+1][c] == 0:
            find_cases(r+1, c+1, 2)
    return


N = int(input()) # (N,N)으로 이동시키는 경우의수
arr = [list(map(int, input().split())) for _ in range(N)]
cnt = 0

find_cases(0, 1, 0)
print(cnt)

