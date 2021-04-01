from collections import deque

delta = [(0, 1), (1, 0), (-1, 0), (0, -1)]

# 바깥 체크
def outside():
    while Q:
        row, col = Q.popleft()
        arr[row][col] = -1
        for dt in range(4):
            new_row = row + delta[dt][0]
            new_col = col + delta[dt][1]
            if 0 <= new_row < r and 0 <= new_col < c and arr[new_row][new_col] == 0:
                arr[new_row][new_col] = -1
                Q.append((new_row, new_col))
    melt_cheese()
    return

# 치즈 녹이기
def melt_cheese():
    cnt = 0
    for row in range(r):
        for col in range(c):
            if arr[row][col] == 1:
                if arr[row-1][col] == -1:
                    arr[row][col] = 0 # 녹은 치즈
                    Q.append((row, col))
                    cnt += 1
                    continue
                if arr[row+1][col] == -1:
                    arr[row][col] = 0  # 녹은 치즈
                    Q.append((row, col))
                    cnt += 1
                    continue
                if arr[row][col-1] == -1:
                    arr[row][col] = 0  # 녹은 치즈
                    Q.append((row, col))
                    cnt += 1
                    continue
                if arr[row][col+1] == -1:
                    arr[row][col] = 0  # 녹은 치즈
                    Q.append((row, col))
                    cnt += 1
                    continue
    if cnt == 0:
        return
    else:
        time.append(cnt)
        outside()

r, c = map(int, input().split())
arr = []
time = [0]
for _ in range(r):
    arr.append(list(map(int, input().split())))

Q = deque([(0, 0)])
outside()
N = len(time)-1
print(N)
print(time[N])
