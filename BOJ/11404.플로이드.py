import sys
input = sys.stdin.readline

N = int(input()) # 도시의 개수
M = int(input()) # 버스의 개수

INF = 0xffffffffffffff
arr = [[INF] * N for _ in range(N)]
for _ in range(M):
    a, b, cost = map(int, input().split())
    arr[a-1][b-1] = min(cost, arr[a-1][b-1])

for k in range(N):
    for i in range(N):
        for j in range(N):
            if i == j:
                arr[i][j] = 0
            else:
                arr[i][j] = min(arr[i][j], arr[i][k] + arr[k][j])

for i in range(N):
    for j in range(N):
        if arr[i][j] == INF:
            arr[i][j] = 0

for line in arr:
    print(*line)