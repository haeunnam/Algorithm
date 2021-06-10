N = int(input())
arr = [0]+[int(input()) for i in range(N)]
ans = []
visited = [0] * (N+1)


def return_to_me(start, next, check):
    if check[next]: return
    if start == next:
        tmp.append(start)
        ans.extend(tmp)
        for i in range(len(tmp)):
            visited[i] = 1
        return
    check[next] = 1
    tmp.append(next)
    return_to_me(start, arr[next], check)
    return


for i in range(1, N+1):
    if i == arr[i]:
        ans.append(i)
    else:
        check = visited[:]
        tmp = []
        return_to_me(i, arr[i], check)
    visited[i] = 1

print(len(ans))
for i in sorted(ans):
    print(i)
