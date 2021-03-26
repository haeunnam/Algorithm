from sys import stdin

n, m = map(int, stdin.readline().split())
## str 정렬순서랑 int정렬은 다름 그러므로 int로 바꿔주는거 필수
nums = list(map(int, stdin.readline().split()))
check = [0] * n
select = [0] * m
ans = []

def comb(idx):
    if idx == m:
        ans.append(tuple(select))
        return
    for i in range(n):
        if check[i] == 0:
            check[i] = 1
            select[idx] = nums[i]
            comb(idx+1)
            check[i] = 0

comb(0)
ans = list(set(ans))
ans.sort()

for i in range(len(ans)):
    for j in range(m):
        print(ans[i][j], end=" ")
    print()


