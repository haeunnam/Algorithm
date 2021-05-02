import sys

sys.stdin = open('input.txt','r')

import sys
from heapq import heappop, heappush
INF = 0xffffffffffffff
def dijkstra(start, end):
    D = [INF] * (N+1)
    heap = [(0, start)]
    D[start] = 0
    while heap:
        d, u = heappop(heap)
        if end == u :
            return D[end]
        if D[u] < d:
            continue

        for v, w in graph[u]:
            new_w = d + w
            if D[v] > new_w:
                D[v] = new_w
                heappush(heap, (new_w, v))

    return D[end]

N = int(input()) # 도시의 개수
M = int(input()) # 버스의 개수
graph = [[] for _ in range(N+1)]
for i in range(M):
    u, v, w = map(int, sys.stdin.readline().split())
    graph[u].append((v, w))

s, e = map(int, input().split())
ans = dijkstra(s, e)

print(ans)