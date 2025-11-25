def factorial(num):
    temp = 1
    for i in range(1, num+1):
        temp *= i
    return temp


def solution(balls, share):
    answer = 0
    answer = factorial(balls) / factorial(balls-share) / factorial(share)
    
    return answer