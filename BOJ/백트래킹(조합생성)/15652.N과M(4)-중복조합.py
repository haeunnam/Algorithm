#### 중복조합
def comb_with_rep(idx, start):
    if idx == M:
        print(" ".join(map(str, choice)))
        return
    for i in range(start, N):
        choice[idx] = i+1
        comb_with_rep(idx+1, i)

N, M = map(int, input().split())
choice = [0] * M

comb_with_rep(0, 0)