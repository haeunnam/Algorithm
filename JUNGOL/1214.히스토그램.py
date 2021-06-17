
arr = list(map(int, input().split()))
N = arr[0]
arr = arr[1:]
max_area = 0
stack = []
area = 0

for idx in range(N):
    cur_h = arr[idx]
    # 스택이 비어있지 않고, 현재 막대기의 높이가 스택 맨 위 높이보다 작을 떄,
    while stack and stack[-1][0] > cur_h:
        h, h_idx = stack.pop()
        width = idx
        if stack:
            width = idx - stack[-1][1] - 1
        area = h * width
        if max_area < area:
            max_area = area
    stack.append((cur_h, idx))

### 배열 끝에 0을 붙이면 아래 코드 대체 가능
while stack:
    h, h_idx = stack.pop()
    area = h * (N - h_idx)
    if max_area < area:
        max_area = area
print(max_area)

