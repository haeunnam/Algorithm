# 재귀로 돌리고
# 중복 안되고 오름차순이므로(앞에 값 뒤에서 뽑는 거 X)이므로 뽑은 값 뒤부터 뽑기 시작
# visited 는 숫자의 중복이 되지 않도록 하는것일 뿐

arr = list(map(int, input().split()))
K = arr[0]
arr = arr[1:]
visited = [0] * 6
sel = [0] * 6

def lotto(idx, start):
    if idx == 6:
        print(*sel)
        return
    for i in range(start, K):
        sel[idx] = arr[i]
        lotto(idx+1, i+1)

lotto(0, 0)