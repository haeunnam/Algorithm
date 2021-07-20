# 딕셔너리 사용하여 USED 표시 하기, kind +1 남은 뽑기 -1
# 이미 뽑은 거면 넘어가기
# 다 돌면 kinds return

def solution(ponketmons):
    rest = len(ponketmons) // 2
    used = dict()
    kinds = 0
    for ponket in ponketmons:
        if ponket in used:
            continue
        else:
            used[ponket] = 1
            kinds += 1
            rest -= 1
        if rest == 0:
            break
    return kinds

