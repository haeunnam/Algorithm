import sys

N = int(sys.stdin.readline())
areas = []
safe = 0
gray_area = [[0]* N for _ in range(N)]
safe_area = [[0]* N for _ in range(N)]
delta = [(1, 0), (-1, 0), (0, 1), (0, -1)]
stack = []


# 물에 잠기는 지역 찾기
def check_gray_areas():
    global safe
    height = min_h
    while True:
        if height > max_h : break
        for i in range(N):
            for j in range(N):
                if gray_area[i][j] <= height:
                    gray_area[i][j] = 0

        for i in range(N):
            for j in range(N):
                safe_area[i][j] = gray_area[i][j]
        ans = find_safe_area()
        if safe < ans :
            safe = ans
        height += 1

    return safe


# 잠기는 지역 제외한 안전영역 갯수 세기
def find_safe_area():
    cnt = 0
    for i in range(N):
        for j in range(N):
            if safe_area[i][j] != 0:
                cnt += 1
                stack = [(i, j)]
                safe_area[i][j] = 0
                while stack:
                    r, c = stack.pop()
                    for dt in range(4):
                        nr = r + delta[dt][0]
                        nc = c + delta[dt][1]
                        if 0 <= nr < N and 0 <= nc < N and safe_area[nr][nc] != 0:
                            safe_area[nr][nc] = 0
                            stack.append((nr, nc))
    return cnt


for i in range(N):
    areas.append(list(map(int, sys.stdin.readline().split())))


# 최대 최솟값 찾기
min_h = 101
max_h = 0
for i in range(N):
    for j in range(N):
        if areas[i][j] < min_h :
            min_h = areas[i][j]
        if areas[i][j] > max_h:
            max_h = areas[i][j]

for i in range(N):
    for j in range(N):
        gray_area[i][j] = areas[i][j]

if min_h == max_h:
    print(1)
else:
    print(check_gray_areas())



#### 발전 시킨 풀이
#### 회색 영역 계산없이 높이를 이용해 바로 안전영역 갯수 세기


def find_safe_area(min_h, max_h):
    ans = 0
    height = min_h
    while height < max_h:
        visited = [[0] * N for _ in range(N)]
        cnt = 0
        for i in range(N):
            for j in range(N):
                if areas[i][j] > height and visited[i][j] == 0:
                    cnt += 1
                    stack = [(i, j)]
                    visited[i][j] = 1
                    while stack:
                        r, c = stack.pop()
                        for dt in range(4):
                            nr = r + delta[dt][0]
                            nc = c + delta[dt][1]
                            if 0 <= nr < N and 0 <= nc < N and visited[nr][nc] == 0:
                                if areas[nr][nc] > height:
                                    visited[nr][nc] = 1
                                    stack.append((nr, nc))
        if ans < cnt:
            ans = cnt
        height += 1

    return ans


N = int(sys.stdin.readline())
areas = []
delta = [(1, 0), (-1, 0), (0, 1), (0, -1)]
stack = []

for i in range(N):
    areas.append(list(map(int, sys.stdin.readline().split())))


# 최대 최소 구하기
min_h = 101
max_h = 0
for i in range(N):
    for j in range(N):
        if areas[i][j] < min_h :
            min_h = areas[i][j]
        if areas[i][j] > max_h:
            max_h = areas[i][j]


if min_h == max_h:
    print(1)
else:
    print(find_safe_area(min_h, max_h))
