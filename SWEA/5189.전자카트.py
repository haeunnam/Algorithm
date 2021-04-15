
# 순열 구하기
def find_ways(idx, battery):
    global min_battery
    if idx == N:
        battery += arr[sel[idx-1]-1][0]
        if min_battery > battery:
            min_battery = battery
        return
    for i in range(2, N+1):
        if visited[i]: continue
        sel[idx] = i # 다음에 갈 곳
        visited[i] = 1
        find_ways(idx+1, battery + arr[sel[idx-1]-1][sel[idx]-1])
        visited[i] = 0
    return


for tc in range(1, int(input())+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * (N+1)
    sel = [1] + [0] * (N-1)
    min_battery = 987654321
    find_ways(1, 0)
    print('#{} {}'.format(tc, min_battery))

