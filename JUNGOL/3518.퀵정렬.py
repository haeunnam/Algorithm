
def quicksort(arr, l, r):
    if l >= r: return
    i = l - 1
    # i는 피봇보다 큰값에서 멈추고, j는 피봇보다 작은 값에서 발동됨
    for j in range(l, r):
        if arr[j] < arr[r]:  #
            i += 1  # 작을 땐 이동하고 큰값일 땐 이동안하므로 큰값에서 멈춤
            arr[i], arr[j] = arr[j], arr[i]  # 작은 값과 교환
    i += 1
    # pivot 자리 찾기
    arr[i], arr[r] = arr[r], arr[i]  # 다 한뒤 피봇보다 큰값 교환, 피봇이 제일 클 때는 본인과 교환됨
    print(*arr)
    quicksort(arr, l, i - 1)
    quicksort(arr, i + 1, r)


N = int(input())
arr = list(map(int, input().split()))
quicksort(arr, 0, N - 1)
