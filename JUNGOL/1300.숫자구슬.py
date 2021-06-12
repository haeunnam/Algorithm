# 분할정복으로... 3개의 그룹일때 최댓값을 이분탐색의 mid로 찾고 이분탐색 돌리기
# start는 숫자들 중 최고 큰거로, end는 total 값으로
# check 함수에서 mid보다 현재까지의 합이 mid보다 작으면 통과 큰 경우 그룹 추가
# 예정된 그룹보다 크면 false, 다 돌렸을 때 작으면 더 돌려보기

def check(max_val, group_num):
    global groups, need_group_split
    groups = []
    group_val = 0
    beads_cnt = 0
    for i in range(N):
        group_val += arr[i]
        beads_cnt += 1
        if group_val > max_val:
            groups.append(beads_cnt - 1)
            beads_cnt = 1
            group_val = arr[i]
            group_num -= 1
            if group_num == -1:
                return False
    else:
        groups.append(beads_cnt)
        group_num -= 1
        if group_num == -1: return False
        need_group_split = group_num
        return True


def regrouping():
    additional_arr = []
    if need_group_split:
        cnt = need_group_split
        for g in range(len(ans_group) - 1, -1, -1):
            while ans_group[g] != 1:
                ans_group[g] -= 1
                additional_arr.append(1)
                cnt -= 1
                if cnt == 0:
                    return additional_arr


N, M = map(int, input().split())  # 구슬의 개수, 그룹의 수
arr = list(map(int, input().split()))  # 구슬에 적혀진 숫자

start = max(arr)
end = sum(arr)
groups = []
ans_group = []
need_group_split = 0

while start <= end:
    mid = (start + end) // 2
    if check(mid, M):
        ans_group = groups[:]
        end = mid - 1
    else:
        start = mid + 1

print(start)
if need_group_split:
    print(*ans_group + regrouping())
else:
    print(*ans_group)