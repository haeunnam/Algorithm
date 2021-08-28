def solution(new_id):
    # 1단계
    answer = new_id.lower()

    # 2단계, 3단계
    tmp = ""
    previous = ""
    for chr in answer:
        if chr in ["-", '_', "."] or chr.isalpha() or chr.isdigit():
            if previous == "." and chr == ".":
                continue
            tmp += chr
            previous = chr
    answer = tmp

    # 4단계
    if len(answer) > 1:
        if answer[0] == ".":
            answer = answer[1:]
        if answer[-1] == ".":
            answer = answer[:-1]
    elif len(answer) == 1:
         if answer[0] == ".":
            answer = ""


    # 5단계
    if answer == "": answer = "a"

    # 6단계
    if len(answer) > 15:
        answer = answer[:15]
        if answer[-1] == ".":
            answer = answer[:-1]

    # 7단계
    while len(answer) <= 2:
        answer += answer[-1]
    print(answer)
    return answer