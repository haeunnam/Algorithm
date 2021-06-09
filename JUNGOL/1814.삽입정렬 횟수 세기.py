N = int(input())
arr = list(map(int, input().split()))

cnt = 0
for i in range(1, N):
    val = arr[i]
    idx = 0
    for j in range(i, 0, -1):
        if val < arr[j-1]:
            arr[j] = arr[j-1]
            cnt += 1
        else:
            idx = j
            break
    arr[idx] = val

print(cnt)
