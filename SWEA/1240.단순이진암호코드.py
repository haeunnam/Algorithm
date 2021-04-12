
# 암호코드 범위 구하기
def code_range():
    for i in range(N):
        for j in range(M - 1, -1, -1):
            if arr[i][j] == '1':
                return (i, j - 56 + 1)

code = ['3211','2221','2122', '1411', '1132', '1231','1114','1312','1213','3112']
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]
    sr, sc = code_range()
    password = []

    # 암호 숫자 구하기
    for i in range(0, 56, 7):
        cnt = 0
        code_res = ''
        for j in range(6):
            if arr[sr][sc+i+j] == arr[sr][sc+i+j+1] : # 1일떄
                cnt += 1
            else: # 0일때
                cnt += 1
                code_res += str(cnt)
                cnt = 0
        code_res += str(cnt+1)
        for j in range(10):
            if code[j] == code_res:
                password.append(j)


    # 암호 숫자 검증하기
    odds = 0
    evens = 0
    for i in range(7):
        if i % 2:
            evens += password[i]
        else:
            odds += password[i]
    ans = odds* 3 + evens + password[7]


    # 올바른 암호코드 판단
    if ans % 10 == 0:
        print(f'#{tc} {sum(password)}')
    else:
        print(f'#{tc} 0')

