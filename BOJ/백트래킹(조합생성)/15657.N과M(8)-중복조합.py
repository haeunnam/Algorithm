#### 중복조합

N, M = map(int, input().split())
num = list(map(int, input().split()))
num.sort()
select = [0] * M

def comb(idx, start):
    if idx == M:
        print(" ".join(map(str, select)))
        return
    for i in range(start, N):
        select[idx] = num[i]
        comb(idx+1, i)

comb(0, 0)

