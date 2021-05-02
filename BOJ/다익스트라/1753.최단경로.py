
import sys
from heapq import heappop, heappush
INF = 0xffffffffffffffffff

def dijkstra(start):
    D = [INF] * (V + 1)
    visited = [0] * (V+1)
    D[start] = 0
    heap = [[0, start]]
    while heap:
        d, u = heappop(heap)
        if visited[u]: continue
        visited[u] = 1

        for v, w in G[u]:
            new_w = D[u] + w
            if not visited[v] and D[v] > D[u] + w:
                D[v] = new_w
                heappush(heap, (D[v], v))
    return D[1:]



V, E = map(int, sys.stdin.readline().split()) # 정점, 간선
K = int(input()) # 시작정점
G = [[] for _ in range(V+1)]
for i in range(E):
    u, v, w = map(int, sys.stdin.readline().split())
    G[u].append((v, w))

ans = dijkstra(K)

for i in ans:
    print(i if i!= INF else 'INF')
