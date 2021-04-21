import sys
sys.stdin = open('input.txt', 'r')

def make_hamburgers(idx, score, calories, passed_score):
    global max_score
    if calories > L: return
    if score + total_score - passed_score < max_score : return
    if idx == N:
        if max_score < score:
            max_score = score
        return
    make_hamburgers(idx+1, score+ingredients[idx][0], calories+ingredients[idx][1], passed_score+ingredients[idx][0])
    make_hamburgers(idx+1, score, calories, passed_score+ingredients[idx][0])


for tc in range(1, int(input())+1):
    N, L = map(int, input().split()) # 재료의 수, 제한 칼로리
    ingredients = [list(map(int, input().split())) for _ in range(N)]
    max_score = 0
    total_score = 0
    for i in range(N):
        total_score += ingredients[i][0]
    make_hamburgers(0, 0, 0, 0)
    print('#{} {}'.format(tc, max_score))

#### 비트로 풀기

def make_hamburgers():
    max_score = 0
    for i in range(1 << N):
        score = 0
        calories = 0
        for j in range(N):
            if i & (1 << j): # 들어 있는지 아닌지
                score += ingredients[j][0]
                calories += ingredients[j][1]
        if calories <= L and max_score < score:
            max_score = score
    return max_score


for tc in range(1, int(input()) + 1):
    N, L = map(int, input().split())  # 재료의 수, 제한 칼로리
    ingredients = [list(map(int, input().split())) for _ in range(N)]
    print('#{} {}'.format(tc, make_hamburgers()))

