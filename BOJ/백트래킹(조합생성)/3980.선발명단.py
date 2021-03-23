
## 어떻게 시간을 줄이지..?
# 아무리 더해도 현재보다 가망 없으면 가지 말기..?

def get_max(idx, cur_sum):
    global max_sum
    if idx == 11:
        if cur_sum > max_sum:
            max_sum = cur_sum
        return

    for j in range(11):
        if check[j]: continue
        if sportsman[idx][j]:
            check[j] = 1
            get_max(idx+1, cur_sum+sportsman[idx][j])
            check[j] = 0


T = int(input())

for _ in range(T):
    sportsman = []
    check = [0] * 11
    max_sum = 0
    for i in range(11):
        sportsman.append(list(map(int, input().split())))
    get_max(0, 0)

    print(max_sum)