def solution(str1, str2):
    answer = 0
    str1List = []
    str2List = []
    for i in range(len(str1) - 1):
        new = str1[i:i + 2]
        if new.isalpha():
            str1List.append(new.lower())

    for i in range(len(str2) - 1):
        new = str2[i:i + 2]
        if new.isalpha():
            str2List.append(new.lower())

    intersection = 0
    total = len(str1List) + len(str2List)

    # 교집합 합집합 구하기
    for chr1 in str1List:
        for chr2 in str2List:
            if chr1 == chr2:
                del str2List[str2List.index(chr2)]
                intersection += 1
                break

    total -= intersection
    if total == 0 and intersection == 0:
        answer = 65536
    else:
        answer = int(intersection/ total * 65536)
    return answer

