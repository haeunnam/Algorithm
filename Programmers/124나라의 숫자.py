def solution(n):
    numbers = ["4", "1", "2", "4"]
    answer = ''
    while n > 3:
        order = n % 3
        n = n // 3
        answer = numbers[order] + answer
        if order == 0:
            n -= 1
    answer =numbers[n]+answer
    print(answer)
    return answer

