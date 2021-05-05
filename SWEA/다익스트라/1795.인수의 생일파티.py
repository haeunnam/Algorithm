
from collections import deque
INF = int(1e9)

def dijkstra(start, graph):
    D = [INF] * (n + 1)
    D[start] = 0
    Q = deque()
    Q.append(start)
    while Q:
        node = Q.popleft()
        for n_node, w in graph[node]:
            d = D[node] + w
            if d < D[n_node]:
                D[n_node] = d
                Q.append(n_node)
    return D[1:]


for tc in range(1, int(input()) + 1):
    n, m, x = map(int, input().split())
    go, come = [[] for _ in range(n + 1)], [[] for _ in range(n + 1)]
    for _ in range(m):
        s, e, w = map(int, input().split())
        come[s].append((e, w)) # 집에 돌아올 때
        go[e].append((s, w)) # 생일 파티 갈때

    ans = max(a + b for a, b in zip(dijkstra(x, go), dijkstra(x, come)))
    print('#{} {}'.format(tc, ans))