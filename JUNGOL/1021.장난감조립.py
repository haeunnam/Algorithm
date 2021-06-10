toy_num = int(input())
M = int(input())
toy_parts = [0] * (toy_num+1)
parts_relation = [[] for i in range(toy_num+1)]
middle_parts = []

for _ in range(M):
    a, b, num = map(int, input().split())
    parts_relation[a].append([b, num])

for i in range(len(parts_relation)):
    if parts_relation[i]:
        middle_parts.append(i)

def find_parts_num(cur_part):
    # 기초부품인 경우는 내비두기
    if cur_part not in middle_parts:
        return
    # 중간부품인 경우는 기초부품으로 만들기
    if toy_parts[cur_part]:
        for relation in parts_relation[cur_part]:
            toy_parts[relation[0]] += relation[1] * toy_parts[cur_part]
            find_parts_num(relation[0])
        toy_parts[cur_part] = 0

toy_parts[toy_num] = 1
find_parts_num(toy_num)

for i in range(toy_num):
    if toy_parts[i]:
        print(i, toy_parts[i])