def solution(num_list):
    answer = 0
    num1 = 0
    num2 = 0
    for idx, i in enumerate(num_list):
        if idx % 2 == 1:
            num1 += i
        else:
            num2 += i
    if num1 > num2:
        answer = num1
    else:
        answer = num2
        
    return answer