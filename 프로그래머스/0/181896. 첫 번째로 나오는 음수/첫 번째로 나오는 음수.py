def solution(num_list):
    answer = 0
    for idx, val in enumerate(num_list):
        if val < 0:
            answer = idx
            break
        else:
            answer = -1

    return answer