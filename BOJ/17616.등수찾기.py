import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

def dfs(x, graph):
    global cnt
    for nx in graph[x]:
        if visited[nx]: continue
        visited[nx] = 1
        cnt += 1
        dfs(nx, graph)
    return
N, M, X = map(int, input().split()) #N명, M번 질문,  X 찾고싶은 학생
high_graph = [[] for _ in range(N+1)]
low_graph = [[] for _ in range(N+1)]
visited = [ 0 for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    high_graph[b].append(a)
    low_graph[a].append(b)

high = 0
low = 0
cnt = 0

dfs(X, high_graph)
high = cnt
cnt = 0
dfs(X, low_graph)
low = cnt
print(high+1, N-low)


