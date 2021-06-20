
def bishop(idx, chess, NUM, cnt):
    global max_cnt
    if cnt + (NUM-idx) < max_cnt: return
    if idx == NUM:
        max_cnt = cnt
        return
    r, c = chess[idx]
    if not diagonal_right[r+c] and not diagonal_left[(c-r)+N-1]:
        diagonal_right[r + c] = 1
        diagonal_left[(c-r)+N-1] = 1
        bishop(idx+1, chess, NUM, cnt+1)
        diagonal_right[r + c] = 0
        diagonal_left[(c-r)+N-1] = 0
    bishop(idx+1, chess, NUM, cnt)


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

# 흰색판, 검은색 판 나누기
white = []
black = []
for i in range(N):
    for j in range(N):
        if arr[i][j]:
            if (i+j) % 2:
                white.append((i, j))
            else:
                black.append((i, j))


diagonal_left = [0]* (N*2-1)
diagonal_right = [0]* (N*2-1)

ans = 0
max_cnt = 0
bishop(0, white, len(white), 0)
ans += max_cnt

max_cnt = 0
bishop(0, black, len(black), 0)
ans += max_cnt
print(ans)
