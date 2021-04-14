import sys
sys.stdin = open('input.txt', 'r')

def count(v, cnt):
    global flag
    if flag : return
    if v == 0: return
    if v == p2:
        flag = cnt
        return
    for i in range(len(people[v])):
        if visited[people[v][i]]: continue
        visited[people[v][i]] = 1
        count(people[v][i], cnt+1)
    return



N = int(input()) # 전체사람의 수
p1, p2 = map(int, input().split()) # 두사람의 번호
m = int(input()) # 부모자식들 간의 관계의 개수
arr = [list(map(int, input().split())) for _ in range(m)] # 부모 / 자식

people = [[] for _ in range(N+1)]
visited = [0] * (N+1)
flag = 0
for i in range(m):
    people[arr[i][0]].append(arr[i][1])
    people[arr[i][1]].append(arr[i][0])

visited[p1] = 1
count(p1, 1)
print(flag-1)
