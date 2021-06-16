import sys
input = sys.stdin.readline
N = int(input())
stack = []
ans = 0
# -1의 값이 새로운 숫자보다 크면 새로운 숫자 stack에 추가
# -1 값이 작을 경우, 나오고 해당 숫자 갯수 계산

for idx in range(N):
    new = int(input())
    while stack and stack[-1][0] <= new:
        pre_cow, pre_idx= stack.pop()
        ans += (idx - pre_idx - 1)
    stack.append((new, idx))

while stack:
    cow, index = stack.pop()
    ans += (N - index - 1)

print(ans)


