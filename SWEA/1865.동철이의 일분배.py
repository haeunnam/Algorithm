

def work(idx, probability):
    global ans
    if probability <= ans: return
    if idx == N:
        if ans < probability:
            ans = probability
        return
    for i in range(N):
        if check[i] or arr[idx][i] == 0 : continue
        check[i] = 1
        work(idx+1, probability * arr[idx][i]/100)
        check[i] = 0
    return

for tc in range(1, int(input())+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    check = [0] * N
    ans = 0
    work(0, 100)
    print('#%d %.6f' % (tc, round(ans, 6)))