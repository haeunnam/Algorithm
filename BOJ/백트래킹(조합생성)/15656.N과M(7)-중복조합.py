#### 중복조합

N, M = map(int, input().split())
num = list(map(int, input().split()))
num.sort()

select = [0] * M

def comb(idx):
    if idx == M:
        print(" ".join(map(str, select)))
        return
    for i in range(N):
        select[idx] = num[i]
        comb(idx+1)

comb(0)

##### 다른 풀이방법


def comb_with_list(idx, ans):
    if idx == M:
        print(*ans)
        return
    for i in range(N):
        comb_with_list(idx+1, ans+[num[i]])

comb_with_list(0, [])