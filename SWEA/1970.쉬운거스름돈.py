
def calculate_change(money, idx):
    if money < 10:
        return
    while money >= unit[idx]:
        money -= unit[idx]
        change[idx] += 1
    calculate_change(money, idx+1)
    return


for tc in range(1, int(input())+1):
    money = int(input())
    change = [0] * 8
    unit = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    calculate_change(money, 0)
    print('#{}'.format(tc))
    print(" ".join(map(str, change)))

