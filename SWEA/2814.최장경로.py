import sys
sys.stdin = open('input.txt', 'r')

def find_longway(v, dist):
    global max_dist
    if max_dist < dist:
        max_dist = dist
    for adj_v in graph[v]:
        if visited[adj_v]: continue
        visited[adj_v] = 1
        find_longway(adj_v, dist + 1)
        visited[adj_v] = 0
    return

for tc in range(1, int(input())+1):
    N, M = map(int, input().split()) # N개의 정점과 M개의 간선
    arr = [list(map(int, input().split())) for _ in range(M)]
    graph = [[] for _ in range(N+1)]
    max_dist = 1

    for i in range(0, M):
        graph[arr[i][0]].append(arr[i][1])
        graph[arr[i][1]].append(arr[i][0])
    for i in range(1, N+1):
        visited = [0] * (N + 1)
        visited[i] = 1
        find_longway(i, 1)
    print('#{} {}'.format(tc, max_dist))