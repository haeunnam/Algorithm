
def find_minsum(r, c, cur_sum):
    global ans
    if cur_sum > ans: return
    if r == N-1 and c == N-1:
        if ans > cur_sum:
            ans = cur_sum
        return
    if r+1 < N and arr[r+1][c]:
        find_minsum(r+1, c, arr[r+1][c]+cur_sum)
    if c+1 < N and arr[r][c+1]:
        find_minsum(r, c+1, arr[r][c+1]+cur_sum)
    return


for tc in range(1, int(input())+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = 987654321
    find_minsum(0, 0, arr[0][0])
    print('#{} {}'.format(tc, ans))



