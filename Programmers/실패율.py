def solution(N, stages):
    failUser = {}
    restUser = len(stages)
    validStages = set()
    check = [0] * (N+2)

    for i in range(len(stages)):
        if stages[i] > N: continue
        validStages.add(stages[i])
        if failUser.get(stages[i]):
            failUser[stages[i]] += 1
        else:
            failUser[stages[i]] = 1
    newValidStages = sorted(list(validStages))
    for stage in newValidStages:
        if failUser.get(stage):
            tmp = failUser[stage]
            failUser[stage] = failUser[stage]/restUser
            restUser -= tmp

    answer = []
    for _ in failUser:
        max_val = 0
        max_stage = 0
        for stage in newValidStages:
            if failUser[stage] > max_val:
                max_val = failUser[stage]
                max_stage = stage
        if max_val:
            failUser[max_stage] = -1
            answer.append(max_stage)
            check[max_stage] = 1

    print(answer)
    for i in range(1, N+1):
        if check[i] == 0:
            answer.append(i)

    print(answer)
    return answer

solution(4, [4, 4, 4, 4, 4])