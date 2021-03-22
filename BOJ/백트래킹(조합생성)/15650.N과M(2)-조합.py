#### 조합

def comb(idx, start):
    if idx == M:
        print(" ".join(map(str, select)))
        return
    for i in range(start, N):
        select[idx] = i+1
        comb(idx+1, i+1)


N, M = map(int, input().split())
select = [0] * M



comb(0, 0)