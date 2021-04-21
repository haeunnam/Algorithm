

def production_cost(idx, cur_cost, check):
    global min_cost
    if min_cost < cur_cost: return
    if idx == N:
        if min_cost > cur_cost:
            min_cost = cur_cost
        return
    for i in range(N):
        if check & (1<<i): continue
        production_cost(idx+1, cur_cost+arr[idx][i], check|(1<<i))
    return

for tc in range(1, int(input())+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    check = [0] * N
    min_cost = 1500
    production_cost(0, 0, 0)
    print('#{} {}'.format(tc, min_cost))