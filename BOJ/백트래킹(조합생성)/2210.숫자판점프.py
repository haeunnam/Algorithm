# 순열
import sys
sys.setrecursionlimit(100000)
delta = [(1, 0), (-1, 0), (0, 1), (0, -1)]
ans_nums = set()
cnt = 0
arr = []
for i in range(5):
    arr.append(list(input().split()))

def dfs(idx, ans, r, c):
    if idx == 5:
        ans_nums.add(ans)
        return
    for dt in range(4):
        nr = r + delta[dt][0]
        nc = c + delta[dt][1]
        if 0 <= nr < 5 and 0 <= nc <5:
            dfs(idx+1, ans+arr[nr][nc], nr, nc)


for i in range(5):
    for j in range(5):
        dfs(0, arr[i][j], i, j)

print(len(ans_nums))