def solution(my_string):
    answer = 0
    
    mode = 0
    temp = ""
    for i in my_string:
        if i in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            temp += i
            print(temp)
        else:
            if temp:
                answer += int(temp)
                temp = ""
    if temp:
        answer += int(temp)
    return answer