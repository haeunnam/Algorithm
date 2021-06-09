N = int(input())
arr = list(map(int, input().split()))

for i in range(N-1):
    min = arr[i]
    min_idx = i
    for j in range(i+1, N):
        if min > arr[j]:
            min = arr[j]
            min_idx = j
    arr[i], arr[min_idx] = arr[min_idx], arr[i]
    print(*arr)
