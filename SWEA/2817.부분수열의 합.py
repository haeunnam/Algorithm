

def subset(idx, start, cur_sum):
    global cnt
    if idx == N:
        return
    if cur_sum == K:
        cnt += 1
        return
    for i in range(start, N):
        subset(idx+1, i+1, cur_sum + arr[i])


for tc in range(1, int(input())+1):
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))
    cnt = 0
    subset(0, 0, 0)
    print(f'#{tc} {cnt}')