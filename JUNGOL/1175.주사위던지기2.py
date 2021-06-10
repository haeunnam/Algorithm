N, M = map(int, input().split())

# 재귀로 돌려서 뽑았을 때 M인 경우만 출력
# 백트래킹 사용해서 시간 줄이기
def make_sum(idx, cur_sum, sel):
    if M-cur_sum > (N-idx) * 6: return
    if idx == N:
        if cur_sum == M:
            print(sel)
        return
    for i in range(1, 7):
        make_sum(idx+1, cur_sum+i, sel+str(i)+' ')

make_sum(0, 0, '')

