def solution(numbers):
    answer = 0
    numbers.sort()
    num1 = numbers[0] * numbers[1]
    num2 = numbers[-1] * numbers[-2]
    
    if num1 > num2:
        answer = num1
    else:
        answer = num2
    
    return answer