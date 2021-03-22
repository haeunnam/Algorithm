#### 부분집합의 합 -> 조합


def subset(idx ,cur_sum, start):
    global flag
    if flag == 1: return
    if idx == 7:
        if cur_sum == 100:
            flag = 1
            select.sort()
            for i in select:
                print(i)
            return 1
        return
    for i in range(start, 9):
        select.append(dwarfs[i])
        subset(idx+1, cur_sum+dwarfs[i], i+1)
        select.pop()

select = []
dwarfs = []
flag = 0
for i in range(9):
    dwarfs.append(int(input()))



subset(0, 0, 0)