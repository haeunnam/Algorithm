def dfs(v):
    global ans
    if v == 0: return
    dfs(L[v])
    ans += P[v]
    dfs(R[v])


for tc in range(1, 11):
    V = int(input())
    L = [0] * (V + 1)  # 부모에서 자식 노드
    R = [0] * (V + 1)
    P = [0] * (V + 1)
    ans = ''
    for i in range(V):
        arr = list(input().split())
        p = int(arr[0])
        P[p] = arr[1]
        if len(arr) == 4:
            L[p] = int(arr[2])
            R[p] = int(arr[3])
        elif len(arr) == 3:
            L[p] = int(arr[2])

    dfs(1)
    print(f'#{tc} {ans}')