n = int(input())

def factorial(x):
    if x == 1:
        print('1! = 1')
        return 1
    print(f'{x}! = {x} * {x-1}!')
    return x * factorial(x-1)

print(factorial(n))