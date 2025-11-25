def solution(n):
    answer = 0
    answer = 2
    for i in range(1, n+1):
        if n % i == 0 and i * i == n:
            print(1)
            answer = 1
        
    return answer