### 시간초과..파이썬의 단점

def diagonal(row, col):
    for i in range(row):
        if row - i == abs(col-picked[i]):
            return True
    return False

def N_queen(idx):
    global ans
    if idx == N:
        ans += 1
        return
    for i in range(N):
        if cols[i] or diagonal(idx, i): continue
        cols[i] = 1
        picked[idx] = i
        N_queen(idx+1)
        cols[i] = 0

N = int(input())
cols = [0] * N
picked = [0 for _ in range(N)]
ans = 0
N_queen(0)
print(ans)
