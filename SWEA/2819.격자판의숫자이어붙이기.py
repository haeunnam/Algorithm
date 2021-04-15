delta = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def make_number(r, c, idx):
    if idx == 7:
        nums.add("".join(sel))
        return
    for dt in range(4):
        nr = r + delta[dt][0]
        nc = c + delta[dt][1]
        if 0 > nr or 0 > nc or 4 <= nr or 4 <= nc: continue
        sel[idx] = arr[nr][nc]
        make_number(nr, nc, idx+1)
    return


for tc in range(1, int(input())+1):
    arr = [input().split() for _ in range(4)]
    sel = [-1] * 7
    nums = set()
    for i in range(4):
        for j in range(4):
            sel[0] = arr[i][j]
            make_number(i, j, 1)

    print('#{} {}'.format(tc, len(nums)))
