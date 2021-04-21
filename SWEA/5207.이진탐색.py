
def binary_search(l, r):
    for i in range(M):
        s, e = l, r
        previous = 0
        cnt = 0
        target = B[i]
        while s <= e:
            mid = (s + e) // 2
            if A[mid] == target:
                ans.append(target)
                break
            elif A[mid] < target:
                s = mid + 1
                if previous == -1: break
                previous = -1
            else:
                e = mid - 1
                if previous == 1: break
                previous = 1
    return


for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split()) # A, B에 속한 정수
    A = list(map(int, input().split()))
    A.sort()
    B = list(map(int, input().split()))
    ans = []
    binary_search(0, N-1)
    print('#{} {}'.format(tc, len(ans)))
