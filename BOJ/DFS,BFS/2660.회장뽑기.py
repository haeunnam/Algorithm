
from collections import deque

N = int(input())
graph = [[] for _ in range(N+1)]
min_score = 51
candidate = []
while True:
    person1, person2 = map(int, input().split())
    if person1 == -1:
        break
    graph[person1].append(person2)
    graph[person2].append(person1)


def BFS(s, graph):
    global min_score, candidate
    visited = [0] * (N+1)
    Q = deque()
    Q.append(s)
    visited[s] = 1
    while Q:
        v = Q.popleft()
        for node in graph[v]:
            if visited[node] == 0:
                visited[node] = visited[v] + 1
                Q.append(node)
        if len(Q) == 0:
            score = visited[v] - 1

            if min_score > score:
                min_score = score
                candidate = [s]
            elif min_score == score:
                candidate.append(s)


# 각 사람마다 점수 체크하기
for start in range(1, N+1):
    BFS(start, graph)

print(min_score, len(candidate))
print(*candidate)