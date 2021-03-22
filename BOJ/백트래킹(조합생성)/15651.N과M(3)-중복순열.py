#### 중복순열

def perm(idx):
    if idx == M:
        print(" ".join(map(str, choice)))
        return
    for i in range(N):
        choice[idx] = num[i]
        perm(idx+1)


N, M = map(int, input().split())
choice = [0] * M
num = [ i for i in range(1, N+1)]


perm(0)