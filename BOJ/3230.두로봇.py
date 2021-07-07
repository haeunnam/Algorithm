import sys
input = sys.stdin.readline

def find_path(x):
    stack = [(x, 0, 0)]
    while stack:
        cx, total, max_cost = stack.pop()
        if cx == b:
            return total - max_cost
        for nx, cost in graph[cx]:
            if visited[nx]: continue
            visited[nx] = 1
            stack.append((nx, total + cost, max_cost if max_cost >= cost else cost))
    return
N, a, b = map(int, input().split())
graph = [[] for _ in range(N+1)]
visited = [0] * (N+1)
for _ in range(N-1):
    c1, c2, cost = map(int, input().split())
    graph[c1].append((c2, cost))
    graph[c2].append((c1, cost))

costs = 0
visited[a] = 1
print(find_path(a))