def calculator():
    for i in range(N):
        new = arr[i]
        if new not in ['+', '-','*','/']:
            stack.append(arr[i])
        else:
            a = int(stack.pop())
            b = int(stack.pop())
            if new == '+':
                stack.append(a+b)
            if new == '-':
                stack.append(b-a)
            if new == '*':
                stack.append(a*b)
            if new == '/':
                stack.append(int(b/a))
    return



N = int(input())
arr = list(input().split())
stack = []
calculator()
print(stack.pop())