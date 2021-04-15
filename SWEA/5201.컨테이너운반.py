
for tc in range(1, int(input())+1):
    N, M = map(int, input().split()) # 컨테이너수, 트럭수
    containers = list(map(int, input().split()))
    truck_cap = list(map(int, input().split()))
    containers.sort(reverse=True)
    truck_cap.sort(reverse=True)

    total = 0
    idx = 0
    for cap in range(M):
        for weight in range(idx, N):
            if truck_cap[cap] >= containers[weight]:
                total += containers[weight]
                idx = weight+1
                break
    print('#{} {}'.format(tc,total))


