#### 조합


def comb(idx, start):
    if idx == M:
        print(" ".join(map(str, choice)))
        return
    for i in range(start, N):
        choice[idx] = num[i]
        comb(idx + 1, i + 1)


N, M = map(int, input().split())
num = list(map(int, input().split()))
num.sort()
choice = [0] * M


comb(0, 0)