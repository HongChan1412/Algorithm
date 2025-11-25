def solution(myString, pat):
    answer = 0
    str_temp = ""
    for i in myString:
        if i == "A":
            str_temp += "B"
        else:
            str_temp += "A"
    
    if pat in str_temp:
        answer = 1
    else:
        answer = 0
    return answer