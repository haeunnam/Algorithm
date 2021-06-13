N = int(input())
arr = list(map(int, input().split()))

def bubble_sort(x):
    for n in range(N-1, 0, -1):
        for i in range(0, n):
            if x[i] > x[i+1]:
                x[i], x[i+1] = x[i+1], x[i]
        print(*arr)

bubble_sort(arr)