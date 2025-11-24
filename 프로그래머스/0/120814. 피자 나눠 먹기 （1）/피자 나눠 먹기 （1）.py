def solution(n):
    answer = 0
    if n <= 7:
        answer = 1
    else:
        while True:
            n = n - 7
            answer += 1
            if n <= 0:
                break
            
    return answer