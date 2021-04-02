# 알던 인접리스트 만들어서 인접리스트 len()이 가장 많은 애 찾아내면되는거아니야?
# 안되네.. 왜나면 제일 멀리있는 친구가 얼마나 걸리는지 모르자나
# 간선의 갯수를 계싼해야겠네 한명씩
# import sys
# sys.stdin = open('input.txt', 'r')

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

#  최소 갯수, BFS

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

for start in range(1, N+1):
    BFS(start, graph)

print(min_score, len(candidate))
print(*candidate)