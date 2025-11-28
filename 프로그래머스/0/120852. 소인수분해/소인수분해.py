def solution(n):
    answer = []
    tf = True
    while tf:
        tf = False
        for i in range(2, n):
            if n % i == 0:
                answer.append(i)
                n = int(n / i)
                tf = True
                break
    answer.append(n)
    answer = list(set(answer))
    answer.sort()
    return answer