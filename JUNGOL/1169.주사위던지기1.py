N, M = map(int, input().split())
sel = [0] * N
def recursive(idx):
    if N == idx:
        print(*sel)
        return
    for i in range(1, 7):
        sel[idx] = i
        recursive(idx+1)

ans = set()
# 리스트로 구해서 정렬시킨 뒤 set에 튜플형식으로 추가
def recursive_without_same_number(idx):
    if N == idx:
        ans.add(tuple(sorted(sel)))
        return
    for i in range(1, 7):
        sel[idx] = i
        recursive_without_same_number(idx+1)

visited = [0] * 7
def recursive_without_duplication(idx):
    if N == idx:
        print(*sel)
        return
    for i in range(1, 7):
        if visited[i]: continue
        visited[i] = 1
        sel[idx] = i
        recursive_without_duplication(idx+1)
        visited[i] = 0


if M == 1:
    recursive(0)
elif M == 2:
    recursive_without_same_number(0)
    ans = sorted(list(ans))
    for i in ans:
        print(*i)
else:
    recursive_without_duplication(0)


