# 순열문제
# 최댓값과 최솟값의 차이 찾기

import sys
sys.stdin = open('0312/input.txt', 'r')

def f(idx, N, ret, op1, op2, op3, op4):
    global max, min
    if idx == N:
        if ret > max:
            max = ret
        if ret < min:
            min = ret
        return
    else:
        if op1 > 0 :
            f(idx+1, N, ret+nums[idx], op1-1, op2, op3, op4)
        if op2 > 0 :
            f(idx+1, N, ret-nums[idx], op1, op2-1, op3, op4)
        if op3 > 0 :
            f(idx+1, N, ret*nums[idx], op1, op2, op3-1, op4)
        if op4 > 0 :
            if ret < 0:
                new_ret = -(-ret // nums[idx])
            else:
                new_ret = ret//nums[idx]
            f(idx+1, N, new_ret, op1, op2, op3, op4-1)


op = ['+', '-', '*', '/']
for tc in range(1, int(input())+1):
    N = int(input())
    op1, op2, op3, op4 = map(int, input().split())
    nums = list(map(int, input().split()))
    min = 9876543210
    max = -9876543210
    f(1, N, nums[0], op1, op2, op3, op4)

    print('#{} {}'.format(tc, max-min))

