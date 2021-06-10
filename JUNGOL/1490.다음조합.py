# 뽑힌 순서는 고려 x
# 1부터 n까지의 정수 중 k개 뽑기 => 조합
# 조합 다음의 조합 수 찾기
# 오름차순 정렬 했을 때, 뽑힌 순서는 고려 X, 넘어가면 끝

# 1. 조합을 먼저 구한다.(배열로 저장)
# 2. 입력받은 조합값을 찾고, 그 다음 조합을 출력

N, K = map(int, input().split())
compare_nums = tuple(map(int, input().split()))

combinations = []
sel = [0] * K
def comb(idx, start):
    if idx == K:
        combinations.append(tuple(sel))
        return
    for i in range(start, N+1):
        sel[idx] = i
        comb(idx+1, i+1)

comb(0, 1)
for i in range(len(combinations)):
    if combinations[i] == compare_nums:
        if i+1 < len(combinations):
            print(*combinations[i+1])
        else:
            print("NONE")

