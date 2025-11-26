def solution(n):
    answer = 0
    temp = 1
    for i in range(1, 11):
        temp *= i
        if temp <= n:
            answer = i
        else:
            break
        
    return answer