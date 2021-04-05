def dfs(v):
    global ans
    if v == 99:
        ans = 1
        return
    for nv in graph[v]:
        if nv not in visited:
            visited.append(nv)
            dfs(nv)
    return

for tc in range(1, 11):
    tc, N = map(int, input().split())
    arr = list(map(int, input().split()))
    graph = [[] for _ in range(101)]
    for i in range(0, N*2, 2):
        graph[arr[i]].append(arr[i+1])
    ans = 0
    visited = []

    dfs(0)
    print(f'#{tc} {ans}')