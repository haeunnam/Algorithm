def solution(progresses, speeds):
    restWork = []
    answer = []
    total = len(progresses)
    for i in range(total):
        if (100 - progresses[i]) % speeds[i]:
            restWork.append((100 - progresses[i]) // speeds[i] + 1)
        else:
            restWork.append((100 - progresses[i]) // speeds[i])

    cnt = 1
    n = 1
    mainFuncDay = restWork[0]
    while n < total:
        if mainFuncDay >= restWork[n]:
            cnt += 1
            n += 1
        else:
            answer.append(cnt)
            mainFuncDay = restWork[n]
            cnt = 1
            n += 1
    answer.append(cnt)
    return answer

solution([93, 30, 55],[1, 30, 5])