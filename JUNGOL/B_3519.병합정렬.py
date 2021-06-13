
def mergeSort(low, high):
    if low >= high: return

    mid = (low+high)//2

    mergeSort(low, mid)
    mergeSort(mid+1, high)

    i, j = low, mid+1
    for k in range(low, high+1):
        if i > mid:
            tmp[k] = arr[j]
            j += 1
        elif j > high:
            tmp[k] = arr[i]
            i += 1
        elif arr[i] <= arr[j]:
            tmp[k] = arr[i]
            i += 1
        else:
            tmp[k] = arr[j]
            j += 1

    for k in range(low, high+1):
        arr[k] = tmp[k]
    print(*arr)

N = int(input())
arr =list(map(int, input().split()))
tmp = [0] * N
mergeSort(0, N-1)
