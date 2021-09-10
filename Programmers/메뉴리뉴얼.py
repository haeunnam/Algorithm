def solution(orders, course):
    answer = []
    candidates = dict()
    def menu_comb(k, start, n, dishes, picked):
        if n == k:
            newComb = "".join(sorted(picked))
            if candidates.get(newComb):
                candidates[newComb] += 1
            else:
                candidates[newComb] = 1
            return
        for i in range(start, len(dishes)):
            picked[k]= dishes[i]
            menu_comb(k+1, i+1, n, dishes, picked)
            picked[k] = 0

    for kinds in course:
        for order in orders:
            menu_comb(0, 0, kinds, order, [0] * kinds)
        maxVal = 0
        keyList = []
        for key, val in candidates.items():
            if val < 2: continue
            if maxVal < val:
                maxVal = val
                keyList = [key]
            elif maxVal == val:
                keyList.append(key)
        candidates = dict()
        answer += keyList

    answer.sort()
    return answer

