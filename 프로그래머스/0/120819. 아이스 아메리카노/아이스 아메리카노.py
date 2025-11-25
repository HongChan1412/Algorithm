def solution(money):
    answer = []
    answer = [0, 0]
    while True:
        if money >= 5500:
            answer[0] += 1
            money -= 5500
        else:
            answer[1] = money
            break
    
    
    return answer