info = input()
stack = []
ans = 0

for i in range(len(info)):
    if info[i] == "(":
        stack.append('(')
    else:
        if info[i-1] == '(':
            stack.pop()
            ans += len(stack)
        else:
            stack.pop()
            ans += 1
print(ans)