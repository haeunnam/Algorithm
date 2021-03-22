## 중복되지 않은 순열

def perm(idx):
    if idx == M:
        print(" ".join(map(str, num)))
        return
    for i in range(N):
        if visited[i] == 0:
            num.append(i+1)
            visited[i] = 1
            perm(idx+1)
            num.pop()
            visited[i] = 0


N, M = map(int, input().split())
num = []
visited = [0 for _ in range(1, N+1)]


perm(0)