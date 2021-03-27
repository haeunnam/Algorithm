from collections import deque

def BFS(n):
    cnt = 0
    Q.append(n)
    while Q:
        for _ in range(len(Q)):
            num = Q.popleft()
            if num == k:
                return cnt
            if num > 100000 or 0 > num: continue
            if visited[num] == 1: continue
            visited[num] = 1

            if num > k :
                Q.append(num - 1)
            else:
                Q.append(num + 1)
                Q.append(num - 1)
                Q.append(num * 2)
        cnt += 1


n, k = map(int, input().split())
Q = deque()
visited = [0] * 100001
print(BFS(n))
