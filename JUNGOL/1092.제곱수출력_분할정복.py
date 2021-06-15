x, y = map(int, input().split())
C = 20091024
def solve(x,y):
    if y == 1:
        return x % C
    if y == 0:
        return 1
    else:
        temp = solve(x, y//2)
        if y % 2 == 0:
            return temp * temp % C  # 짝수인 경우
        else:
            return temp * temp * x % C  # 홀수
print(solve(x, y))