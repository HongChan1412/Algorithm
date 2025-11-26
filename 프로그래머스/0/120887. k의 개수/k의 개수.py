def solution(i, j, k):
    answer = 0
    for num1 in range(i, j+1):
        if str(k) in str(num1):
            for num2 in str(num1):
                if str(k) in num2:
                    answer += 1
    
    return answer