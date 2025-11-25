def solution(n):
    answer = 0
    pizza = 6
    answer = 1
    while True:
        pizza = pizza - n
        if pizza % n == 0:
            break
        pizza = pizza + 6
        answer += 1

    return answer