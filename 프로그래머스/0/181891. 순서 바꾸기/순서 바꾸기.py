def solution(num_list, n):
    answer = []
    for idx, val in enumerate(num_list):
        if idx >= n:
            answer.append(val)
    for idx, val in enumerate(num_list):
        if idx < n:
            answer.append(val)    
    return answer