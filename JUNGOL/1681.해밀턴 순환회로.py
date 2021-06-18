# 1-[2-3-4-5]-1
# 순열로 돌리고, 백트래킹으로 걷어내기

def DFS(idx, cost, cur_loc):
    global min_cost
    if min_cost < cost: return
    if idx == N and arr[cur_loc][0]:
        if min_cost > cost + arr[cur_loc][0]:
            min_cost = cost + arr[cur_loc][0]
        return
    for i in range(1, N):
        if way[i] or not arr[cur_loc][i] : continue
        way[i] =1
        DFS(idx+1, cost+arr[cur_loc][i], i)
        way[i] = 0

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
way = [0] * N
min_cost = 100 * N
DFS(1, 0, 0)
print(min_cost)