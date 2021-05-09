import sys

# 1번 부터 N까지의 최단거리 v1, v2 거쳐서
# 경로없을 때는 1
from heapq import heappop,heappush

INF = int(1e9)
def dijkstra(start, end):
    D = [INF] * (N+1)
    D[start] = 0
    Q = [(0, start)]
    while Q:
        d, u = heappop(Q)
        if D[u] < d: continue
        if u == end : return D[end]

        for v, w in G[u]:
            tmp = d + w
            if D[v] > tmp:
                D[v] = tmp
                heappush(Q, (D[v], v))

    return D[end]


N, E = map(int, sys.stdin.readline().split()) # 정점과 간선
G = [[] for _ in range(N+1)]
for _ in range(E):
    u, v, w = map(int, sys.stdin.readline().split())
    G[u].append((v, w))
    G[v].append((u, w))
v1, v2 = map(int, sys.stdin.readline().split())

ans = min(dijkstra(1, v1) + dijkstra(v1, v2) + dijkstra(v2, N), dijkstra(1, v2) + dijkstra(v2, v1) + dijkstra(v1, N))
if ans >= INF:
    ans = -1

print(ans)