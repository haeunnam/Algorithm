

def promising(r, c):
    nums = [0 for _ in range(10)]
    rest = []
    # 행열 검사
    for i in range(9):
        nums[sudoku[r][i]] = 1
        nums[sudoku[i][c]] = 1

    nr = r //3
    nc = c //3
    # 3*3 박스 검사
    for i in range(nr*3, (nr+1)*3):
        for j in range(nc*3, (nc+1)*3):
            num = sudoku[i][j]
            nums[num] = 1
    #남은 배열
    for i in range(1,10):
        if not nums[i]:
            rest.append(i)
    return rest

def dfs(idx):
    global flag
    if flag:  # 이미 답이 출력된 경우
        return

    if idx == len(blank):
        for row in sudoku:
            print(*row)
        flag = True
        return
    else:
        r, c = blank[idx]
        promising_num = promising(r, c)

        for num in promising_num:
            sudoku[r][c] = num #유망한 숫자중 하나 선택
            dfs(idx+1)
            sudoku[r][c] = 0


sudoku = [list(map(int, input().split())) for _ in range(9)]
blank = []
flag = False
for i in range(9):
    for j in range(9):
        if sudoku[i][j] == 0:
            blank.append([i,j])

dfs(0)