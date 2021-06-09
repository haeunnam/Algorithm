num = int(input())
def hanoi(N, start, via, end):
    if N == 1:
        print(f'1 : {start} -> {end}')
        return
    hanoi(N-1, start, end, via)
    print(f'{N} : {start} -> {end}')
    hanoi(N-1, via, start, end)

hanoi(num, 1, 2, 3)