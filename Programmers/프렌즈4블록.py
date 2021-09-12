def solution(m, n, board):
    answer = 0
    board = [list(board[i]) for i in range(m)]
    removedBlock = set()
    blockCnt = 0
    while True:
        # 2x2 블록 찾기
        for r in range(m-1):
            for c in range(n-1):
                if board[r][c] != 0 and board[r][c] == board[r+1][c] == board[r][c+1] == board[r+1][c+1]:
                    removedBlock.add((r,c))
                    removedBlock.add((r+1,c))
                    removedBlock.add((r,c+1))
                    removedBlock.add((r+1,c+1))
        # 블록 지우기
        if not removedBlock:
            break
        for r, c in removedBlock:
            board[r][c] = 0
            blockCnt += 1
        removedBlock = set()
        # 정렬
        for c in range(n):
            for r in range(m-1, -1, -1):
                if board[r][c] == 0:
                    for dt in range(1, r+1):
                        if board[r-dt][c] != 0:
                            board[r][c],board[r-dt][c] = board[r-dt][c], board[r][c]
                            break
    answer = blockCnt
    return answer


