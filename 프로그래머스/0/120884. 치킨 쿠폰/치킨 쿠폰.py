def solution(chicken):
    answer = -1
    answer = 0
    while True:
        if chicken >= 10:
            answer += chicken // 10
            chicken = chicken % 10 + chicken // 10
        else:
            break
    return answer