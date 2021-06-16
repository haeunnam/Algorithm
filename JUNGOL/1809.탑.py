
N = int(input())
arr = [0] + list(map(int, input().split()))
ans = [0] * (N+1)
stack = []

for i in range(N, 0, -1):
    new = arr[i]
    if not stack:
        stack.append((new, i))
    else:
        # 자기보다 클 때
        while stack and stack[-1][0] < new:
            top_h, top_i = stack.pop()
            ans[top_i] = i
        stack.append((new, i))

while stack:
    top_h, top_i = stack.pop()
    ans[top_i] = 0

print(*ans[1:])