# 일단 하나씩 돌면서 하,우 중 나와 색깔이 다른 사탕인경우를 고른다.
# 교환한 뒤, 전체 배열 중 배열의 사탕이 많은 행 or 열을 찾는다
# max_candy에 비교하고 저장한뒤 다음으로 넘어간다.

def find_candy():
    for i in range(N):
        for j in range(N):
            cur = candies[i][j]
            if j < N-1 and cur != candies[i][j+1]:
                # 스왑
                candies[i][j], candies[i][j+1] = candies[i][j+1], candies[i][j]
                check_candy()
                candies[i][j], candies[i][j+1] = candies[i][j+1], candies[i][j]
            if i < N-1 and cur != candies[i+1][j]:
                candies[i][j], candies[i+1][j] = candies[i+1][j], candies[i][j]
                check_candy()
                candies[i][j], candies[i+1][j] = candies[i+1][j], candies[i][j]

# 전체 캔디가 다돌게
def check_candy():
    global max_candy
    # 가로
    for i in range(N):
        cnt = 1
        for j in range(N-1):
            if candies[i][j] != candies[i][j+1]:
                if max_candy < cnt:
                    max_candy = cnt
                cnt = 1
            else:
                cnt += 1
        if max_candy < cnt:
            max_candy = cnt

    for j in range(N):
        cnt = 1
        for i in range(N-1):
            if candies[i+1][j] != candies[i][j]:
                if max_candy < cnt:
                    max_candy = cnt
                cnt = 1
            else:
                cnt += 1
        if max_candy < cnt:
            max_candy = cnt


N = int(input())
max_candy = 0
candies = []
for _ in range(N):
    candies.append(list(input()))
find_candy()
print(max_candy)
