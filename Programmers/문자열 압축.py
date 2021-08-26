
def solution(s):
    length = len(s) // 2 + 1
    answer = len(s)
    # 얼마만큼의 문자열을 보여줄지
    for cut in range(1, length):
        prev_str = s[:cut]
        cnt = 1
        # 문자열 순환
        new_str = ""
        for j in range(cut, len(s), cut):
            if s[j:j+cut] == prev_str:
                cnt += 1
            else:
                if cnt > 1 :
                    new_str += (str(cnt)+prev_str)
                elif cnt == 1 :
                    new_str += prev_str
                cnt = 1
            prev_str = s[j:j+cut]
        if cnt == 1: cnt = ""
        new_str += (str(cnt)+prev_str)
        answer = min(answer, len(new_str))
    return answer


solution("aabbaccc")
