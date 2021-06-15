# 스택이용
# 자기보다 큰 값이면 pop 하고 빌딩기록, 작은 값일 경우 넣기
import sys
input = sys.stdin.readline

N = int(input())
stack = []
ans = [0] * (N+1)

for idx in range(1, N+1):
    height = int(input())
    if not stack:
        stack.append((idx, height))
    while stack:
        pre_idx, pre_height = stack[-1]
        # 높은 빌딩 나오는 경우
        if height > pre_height:
            stack.pop() # 스택에서 제외시키고
            ans[pre_idx] = idx  # ans에 추가
        # 이전보다 작은빌딩 나오는 경우(높은 빌딩 못찾음)
        else:
            break
    stack.append((idx, height)) # 스택에 추가

while stack:
    i, h = stack.pop()
    ans[i] = 0

for i in range(1, N+1):
    print(ans[i])



################## 풀이2
import sys
input = sys.stdin.readline

from collections import deque

N = int(input())
arr = [0] + [int(input()) for _ in range(N)]

ans = [0] * (N + 1)
Q = deque()
Q.append((N, arr[N]))

for i in range(N - 1, 0, -1):
    this_height = arr[i]
    while Q:
        idx, pre_height = Q.pop()
        if this_height < pre_height:
            ans[i] = idx
            Q.append((idx, pre_height))
            Q.append((i, this_height))
            break
    else:
        ans[i] = 0
        Q.append((i, this_height))

for i in range(1, N + 1):
    print(ans[i])