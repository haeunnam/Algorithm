target = int(input())
broken = int(input())
if broken:
    broken_nums = list(input().split())

# 리모컨으로 이동할 경우
ans = abs(100-target)

# target채널이 최대 500,000이므로 최악의 경우를 고려해서 1,000,000까지 탐색
for i in range(1000001):
    num = str(i)
    for j in range(len(num)):
        # 고장난 버튼이 하나라도 있으면 skip
        if num[j] in broken_nums:
            break
    # 가능한 숫자일 경우
    else:
        # 이동값 계산해서 최소인 것을 저장
        ans = min(ans, abs(i-target) + len(num))
print(ans)