def judge(player):
    cnt = 0
    for i in range(10):
        # 3보다 높은 숫자가 있는지
        if player[i] > 2:
            return True
        # 1이 연속 되었는지
        if player[i]:
            cnt += 1
        else:
            cnt = 0
        if cnt == 3:
            return True
    return False

for tc in range(1, int(input())+1):
    arr = list(map(int, input().split()))
    player1 = [0] * 10
    player2 = [0] * 10
    win = 0
    for i in range(12):
        if i % 2 == 0:
            player1[arr[i]] += 1
            if judge(player1):
                win = 1
        else:
            player2[arr[i]] += 1
            if judge(player2):
                win =  2
        if win:
            break
    print('#{} {}'.format(tc, win))
