
# x번을 문여는 방법 찾기
# 재귀로 돌려서 min_cnt 찾으면
def closet_move(idx, cnt):
    global min_cnt
    if min_cnt < cnt: return
    if idx == N :
        if cnt < min_cnt:
            min_cnt = cnt
        return
    for i in range(len(opend)):
        tmp = opend[i]
        opend[i] = closet[idx]
        closet_move(idx+1, cnt + abs(closet[idx] - tmp))
        opend[i] = tmp

total = int(input())
opend = list(map(int, input().split()))
N = int(input())
closet = []
for i in range(N):
    closet.append(int(input()))
min_cnt = 0xffffffffff

closet_move(0, 0)
print(min_cnt)