#### 순열


def perm(idx):
    if idx == M:
        print(" ".join(map(str, choice)))
        return
    for i in range(N):
        if visited[i] == 0:
            choice[idx] = num[i]
            visited[i] = 1
            perm(idx+1)
            visited[i] = 0


N, M = map(int, input().split())
num = list(map(int, input().split()))
num.sort()
visited = [0] * N
choice = [0] * M

perm(0)