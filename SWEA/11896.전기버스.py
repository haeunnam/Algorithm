
def charge(idx, cur_battery, exchanged):
    global min_val
    if exchanged >= min_val: return
    if cur_battery == 0 : return
    if idx == N-1:
        if min_val > exchanged:
            min_val = exchanged
        return
    charge(idx+1, battery[idx], exchanged+1)
    charge(idx+1, cur_battery-1, exchanged)
    return


for tc in range(1, int(input()) + 1):
    arr = list(map(int, input().split()))
    N = arr[0]
    battery = arr[1:]
    min_val = N + 1
    charge(1, battery[0], 0)
    print('#{} {}'.format(tc, min_val))

