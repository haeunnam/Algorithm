for tc in range(1, int(input())+1):
    N = int(input()) # 신청서
    arr = [list(map(int, input().split())) for _ in range(N)] # 시작시간, 종료시간

    # 1) 끝나는 시간이 빠른 순으로 세우기
    arr.sort(key=lambda x : x[1])

    pick = [arr[0]]
    for i in range(1, N):
        if pick[-1][1] <= arr[i][0]:
            pick.append(arr[i])

    print('#{} {}'.format(tc, len(pick)))