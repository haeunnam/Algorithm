# 분할정복
# 범위 나눠서 아래로 내려가기,(4개의 범위 나누기)
# 파란색인지 하얀색인지 검사, 섞여있으면 범위나누기 진행 아닌경우 파란색이면 blue += 1 하얀색이면 white += 1
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

total_blue = 0
total_white = 0
def is_all_painted(rs, re, cs, ce):
    blue = 0
    white = 0
    for i in range(rs, re):
        for j in range(cs, ce):
            if arr[i][j]:
                blue += 1
            else:
                white += 1
            if blue != 0 and white != 0:
                return -1
    if blue > 0:
        return 1
    elif white > 0:
        return 0


def divide_paper(rs, re, cs, ce):
    global total_blue, total_white
    color = is_all_painted(rs, re, cs, ce)
    if color == -1:
        # 범위 더 들어가기
        mid_r, mid_c = (rs +re)//2, (cs+ce)//2
        divide_paper(rs, mid_r, cs, mid_c)
        divide_paper(rs, mid_r, mid_c, ce)
        divide_paper(mid_r, re, cs, mid_c)
        divide_paper(mid_r, re, mid_c, ce)
    else:
        if color == 1:
            total_blue += 1
        elif color == 0:
            total_white += 1
    return

divide_paper(0, N, 0, N)

print(total_white)
print(total_blue)