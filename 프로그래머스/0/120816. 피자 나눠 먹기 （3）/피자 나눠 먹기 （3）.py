def solution(slice, n):
    answer = 0
    answer = 1
    pizza = slice
    while True:
        if slice >= n:
            break
        slice += pizza
        answer += 1
    
    
        
    return answer