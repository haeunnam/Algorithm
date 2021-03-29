from collections import deque


def BFS():
    ans = 1
    while Q:
        size = len(Q)
        for i in range(size):
            num = Q.popleft()
            if num > b : continue
            if num == b:
                return ans
            if num * 2 <= b :
                Q.append(num * 2)
            tmp = int(str(num) + '1')
            if tmp <= b :
                Q.append(tmp)
        ans += 1
    return -1


a, b = map(int, input().split())
Q = deque()
Q.append(a)
print(BFS())

# ########다른 풀이 b -> a로 가기
# 2를 나누는 것과 뒷자리수 1을 빼는 게 동시에 일어날 수 없음을 이용

a, b= map(int, input().split())
ans = 1
while a!=b and b > a:
    ans += 1
    if b % 10 == 1:
        b //= 10
    elif b % 2 == 0:
        b //= 2
    else:
        print(-1)
        break

else:
    if b < a:
        print(-1)
    else:
        print(ans)
