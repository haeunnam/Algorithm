from heapq import heappush, heappop
INF = 0xffffffffffffffffffffffffffff

# 어떤 시작점에서 모든 정점까지의 최단거리
def dijkstra(start, graph):
    visited = [0] * (N+1)
    D = [INF] * (N+1)
    D[start] = 0
    Q = [(0, start)]
    while Q:
        d, u = heappop(Q)
        if visited[u]: continue
        visited[u] = 1

        for v, t in graph[u]:
            if not visited[v] and D[v] > d + t:
                D[v] = d + t
                heappush(Q, (D[v], v))
    return D[1:]


N, M, X = map(int, input().split())
# N명의 학생, M개의 도로, X 파티하는 장소
go = [[] for _ in range(N+1)]
come = [[] for _ in range(N+1)]

for i in range(M):
    s, e, t = map(int, input().split())
    # 가는 길, 오는 길 경로 그래프 나누기
    go[s].append((e, t))
    come[e].append((s, t))

print(max( a + b for a, b in zip(dijkstra(X, go), dijkstra(X, come))))
