import sys
sys.stdin = open('input.txt', 'r')
# https://www.acmicpc.net/board/view/54133 반례들
def check_areas(check):
    for i in range(1, N+1):
        if check[i] == 0:
            start = i
            break

    stack = [start]
    while stack:
        u = stack.pop()
        if check[u]: continue
        check[u] = 1
        for v in G[u]:
            stack.append(v)
    for i in check[1:]:
        if i == 0:
            return False
    return True


def make_two_areas(lst):
    area1_visited = lst[:]
    area2_visited = [int(not i) for i in area1_visited] # 다른 선거지역
    if not check_areas(area1_visited):
        return False
    if not check_areas(area2_visited):
        return False
    return True


# 조합 백트래킹
def divide_area(idx, population):
    global ans
    if population > total // 2 : return
    if idx == N+1:
        diff = abs(total - population * 2)
        if diff < ans and make_two_areas(visited):
            ans = diff
        return
    visited[idx] = 1
    divide_area(idx + 1, population+arr[idx])
    visited[idx] = 0
    divide_area(idx + 1, population)
    return


# 선거구 나누기
# 두 구역의 인구 최솟값 구하기,  안되는 경우 -1 출력
# 구역 나눌 때 꼭 인접해야 함.

N = int(input()) # 구역의 개수
arr = [0] + list(map(int, input().split())) # 구역의 인구
G = [[] for _ in range(N+1)]
visited = [0] * (N+1)
for i in range(1, N+1):
    adj_area = list(map(int, input().split()))
    for adj in adj_area[1:]:
        G[i].append(adj)
total = sum(arr)
ans = total

divide_area(1, 0)
if total == ans:
    print(-1)
else:
    print(ans)

