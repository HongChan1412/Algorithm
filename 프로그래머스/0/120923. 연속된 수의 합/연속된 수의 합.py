def solution(num, total):
    answer = []
    # answer = [-i for i in range(num)]
    answer = [i for i in range(-num, 0, 1)]
    # answer = answer[::-1]
    while True:
        if sum(answer) == total:
            break
        else:
            answer = [i+1 for i in answer]
        
    return answer