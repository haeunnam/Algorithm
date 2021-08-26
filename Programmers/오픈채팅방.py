def solution(record):
    userInfo = {}
    chatInfo = []
    for sentence in record:
        words = sentence.split(" ")
        type, userId = words[0], words[1]
        if type == "Enter":
            userInfo[userId] = words[2]
            message = "님이 들어왔습니다."
            chatInfo.append([message, userId])
        elif type == "Leave":
            message = "님이 나갔습니다."
            chatInfo.append([message, userId])
        else:
            userInfo[userId] = words[2]

    answer=[]
    for j in range(len(chatInfo)):
        message, userId = chatInfo[j][0], userInfo[chatInfo[j][1]]
        answer.append(userId+message)
    print(answer)
    return answer


solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"])