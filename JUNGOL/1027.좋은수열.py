# 11, 12,12, 123,123  1~ N//2 까지 검사해야함
# 걔중에 길이 작은 것만(백트래킹, 현재구한것중 길이 크면 나가리)


def check(idx, num):
    length = idx
    cnt = length//2
    start = int(length % 2)
    for i in range(start, length, 2):
        if num[i:(i+cnt)] == num[(i+cnt):]:
            return False
        cnt -= 1
    return True


def good_numbers(idx, num):
    global min_val
    if idx and int(str(min_val)[:idx]) < int(num): return
    if idx == N:
        if min_val > int(num):
            min_val = int(num)
        return
    for i in range(1, 4):
        if check(idx+1, num+str(i)):
            good_numbers(idx+1, num+str(i))



N = int(input())
min_val = 4 * (10 ** N)
good_numbers(0, '')
print(min_val)