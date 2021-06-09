from collections import deque

N = int(input())
queue = deque()
for _ in range(N):
    chr = input().split()
    if chr[0] == 'i':
        queue.append(chr[1])
    elif chr[0] == 'o':
        if queue:
            print(queue.popleft())
        else:
            print('empty')
    else:
        print(len(queue))
