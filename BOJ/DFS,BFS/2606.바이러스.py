def DFS(v):
    visited[v] = 1
    stack.append(v)
    while stack:
        for w in Graph[v]:
            if visited[w] == 0:
                visited[w] = 1
                stack.append(v)
                v = w
                break
        else:
            v = stack.pop()
    return sum(visited)-1


V = int(input())
E = int(input())
Graph = [[] for i in range(V+1)]

for _ in range(E):
    s, e = map(int, input().split())
    Graph[s].append(e)
    Graph[e].append(s)
visited = [0] * (V + 1)
stack = []
print(DFS(1))


