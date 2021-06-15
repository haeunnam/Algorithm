import sys
N = int(input())
arr = [sys.stdin.readline().split() for _ in range(N)]
print(arr)
ans = ''
def divide_paper(rs, re, cs, ce):
    global ans
    if rs-re == 1:
        ans += arr[rs][cs]
        return
    else:
        state = paper_state(rs, re, cs, ce)

    if state == -1:
        ans += 'X'
        # 범위나누기
        mid_r, mid_c = (rs+re)//2, (cs+ce)//2
        divide_paper(rs, mid_r, cs, mid_c)
        divide_paper(rs, mid_r, mid_c, ce)
        divide_paper(mid_r, re, cs, mid_c)
        divide_paper(mid_r, re, mid_c, ce)
    else:
        ans += state
        return
    return

def paper_state(rs, re, cs, ce):
    previous = arr[rs][cs]
    for i in range(rs, re):
        for j in range(cs, ce):
            if arr[i][j] != previous:
                return -1
    return previous


divide_paper(0, N, 0, N)
print(ans)