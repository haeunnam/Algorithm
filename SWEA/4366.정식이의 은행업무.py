def compare():
    base2_int = []
    for i in range(len(base2)):
        new = int(base2, 2) ^ 1 << i
        base2_int.append(new)

    for i in range(len(base3)):
        new = list(base3)
        for j in range(3):
            if base3[i] != str(j):
                new[i] = str(j)
                for num in base2_int:
                    if int("".join(map(str, new)), 3) == num:
                        return num


for tc in range(1, int(input()) + 1):
    base2 = input()
    base3 = list(input())
    print('#{} {}'.format(tc, compare()))