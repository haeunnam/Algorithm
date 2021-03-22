import sys
import copy
sys.setrecursionlimit(10000000)


def color_segment():
    stack = []
    arr = copy.deepcopy(array)
    cnt = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] in color:
                cnt += 1
                color_num = color[arr[i][j]]
                arr[i][j] = color_num
                stack.append((i, j))
                while stack:
                    r, c = stack.pop()
                    for k in range(4):
                        nr = r + delta[k][0]
                        nc = c + delta[k][1]
                        if 0 <= nr < N and 0 <= nc < N:
                            if arr[nr][nc] in color and color[arr[nr][nc]] == color_num:
                                arr[nr][nc] = color_num
                                stack.append((nr, nc))
    return cnt


delta = [(1, 0), (-1, 0), (0, 1), (0, -1)]

N = int(input())
array = []
for _ in range(N):
    array.append(list(input()))

color = {'R': 0, 'G': 1, 'B': 2}
normal = color_segment()
color = {'R': 0, 'G': 0, 'B': 2}
color_blindness = color_segment()

print(normal, color_blindness)