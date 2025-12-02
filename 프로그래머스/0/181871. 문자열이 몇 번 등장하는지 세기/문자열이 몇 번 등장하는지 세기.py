def solution(myString, pat):
    answer = 0
    temp_idx = 0
    while (pat in myString):
        myString = myString[myString.find(pat)+1:]
        answer += 1
    
    return answer