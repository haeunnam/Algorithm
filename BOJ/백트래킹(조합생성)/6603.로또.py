

def lotto(idx, start):
    if idx == 6:
        print(" ".join(select))
        return
    for i in range(start, k):
        select[idx] = S[i]
        lotto(idx+1, i+1)

select = [0] * 6

while True:
    nums = list(input().split())
    k, S = int(nums[0]), nums[1:]
    if k == 0:
        break
    lotto(0, 0)
    print()
