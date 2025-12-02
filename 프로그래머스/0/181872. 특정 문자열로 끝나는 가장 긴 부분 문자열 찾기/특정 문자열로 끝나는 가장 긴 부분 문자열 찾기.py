def solution(myString, pat):
    answer = ''
    # if pat in myString:
    answer = myString[:myString.rfind(pat)+len(pat)]
    
    return answer