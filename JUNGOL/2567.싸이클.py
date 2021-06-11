# 1. N 출력 2. (val * N) % P 구하기
# arr 만들어서 구한 val이 이전에 있는지 확인하고, append 시킴, 있는 경우 있는 현재 length - 인덱스
N, P = map(int, input().split())

arr = []
ans = 0
def find_repeated_num(val):
    global ans
    for i in range(len(arr)):
        if val == arr[i] :
            ans = len(arr)- i
            return
    arr.append(val)
    return find_repeated_num((val * N) % P)

find_repeated_num(N)
print(ans)