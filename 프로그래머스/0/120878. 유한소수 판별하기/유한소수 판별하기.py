def solution(a, b):
    answer = 0
    
    
    for i in reversed(range(1, 1001)):
        if a % i == 0 and b % i == 0:
            a = a / i
            b = b / i
    
    temp = 0
    while True:
        temp = b
        if b % 2 == 0:
            b = b / 2
        if b % 5 == 0:
            b = b / 5
        if temp == b:
            break
    if b == 1:
        answer = 1
    else:
        answer = 2
    return answer