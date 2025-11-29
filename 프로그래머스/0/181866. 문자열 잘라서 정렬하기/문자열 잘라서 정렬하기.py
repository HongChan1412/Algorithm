def solution(myString):
    answer = []
    answer = sorted([i for i in myString.split("x") if i])
    return answer