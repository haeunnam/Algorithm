import sys
sys.stdin = open('../JUNGOL/input.txt', 'r')
input = sys.stdin.readline

def dfs(x, graph):
    for next_x in graph[x]:
        if visited[next_x]: continue
        visited[next_x] = 1
        dfs(next_x, graph)
    return

N, M = map(int, input().split()) # 비교한 횟수
# 키 큰 경우와 작은 경우를 나누어 생각
graph_high = [[] for _ in range(N+1)]
graph_low = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph_high[a].append(b)
    graph_low[b].append(a)

ans = 0
for i in range(1, N+1):
    visited = [0] * (N + 1)
    visited[i] = 1
    dfs(i, graph_high)
    dfs(i, graph_low)
    if sum(visited) == N:
        ans += 1

print(ans)

