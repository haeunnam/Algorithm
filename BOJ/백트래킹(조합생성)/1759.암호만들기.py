import sys

# 중복되지 않는 조합, 정렬하기
def make_password(idx, start, vowels, consonants):
    if idx == l:
        if vowels >= 1 and consonants >= 2:
            print("".join(map(str, password)))
        return
    for i in range(start, c):
        password[idx] = chars[i]
        if chars[i] in ['a', 'e', 'i', 'o', 'u']:
            vowels += 1
            make_password(idx+1, i+1, vowels, consonants)
            vowels -= 1
        else:
            consonants += 1
            make_password(idx+1, i+1, vowels, consonants)
            consonants -= 1



l, c = map(int, sys.stdin.readline().split())
chars = list(sys.stdin.readline().split())
chars.sort()
password = [0] * l


make_password(0, 0, 0, 0)
