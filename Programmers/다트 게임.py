def solution(dartResult):
    tmp = 0
    scores = []
    option = ['S', 'D', 'T','*', '#']
    for chr in dartResult:
        # 숫자일 경우
        if chr not in option:
            if tmp == 1:
                tmp = 10
            else:
                tmp = int(chr)
        else:
            if chr == option[0]:
                scores.append(tmp ** 1)
            elif chr == option[1]:
                scores.append(tmp ** 2)
            elif chr == option[2]:
                scores.append(tmp ** 3)
            elif chr == option[3]:
                pre_idx = len(scores) - 1
                if pre_idx != 0:
                    scores[pre_idx-1] = scores[pre_idx-1] * 2
                scores[pre_idx] = scores[pre_idx] * 2
            elif chr == option[4]:
                pre_idx = len(scores) - 1
                scores[pre_idx] = scores[pre_idx] * -1
            tmp = 0
    answer = sum(scores)
    return answer

