T = int(input())

def go(idx, x, y, dist):
    global ans
    if ans < dist: return
    if idx == N:
        dist = dist + abs(x - home_x) + abs(y - home_y)
        if ans > dist:
            ans = dist
        return
    for i in range(0, N*2, 2):
        check = i // 2
        if visited[check] == 0:
            visited[check] = 1
            go(idx+1, arr[i], arr[i+1], dist+abs(x - arr[i]) + abs(y-arr[i+1]))
            visited[check] = 0



for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    visited = [0] * (N + 1)
    work_x, work_y = arr[0], arr[1]
    home_x, home_y = arr[2], arr[3]
    arr = arr[4:]
    ans = 987654321
    go(0, work_x, work_y, 0)
    print('#{} {}'.format(tc, ans))
