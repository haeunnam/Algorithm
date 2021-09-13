def solution(numbers, target):
    global answer
    total = sum(numbers)
    answer = 0
    def find_targetNum(k, n, start, total):
        global answer
        if total < target: return
        if n == k and total == target:
            answer += 1
            return
        for i in range(start, len(numbers)):
            find_targetNum(k + 1, n, i+1, total - numbers[i] * 2)

    for i in range(0, len(numbers)+1):
        find_targetNum(0, i, 0, total)
    return answer

solution([1, 1, 1, 1, 1], 3)