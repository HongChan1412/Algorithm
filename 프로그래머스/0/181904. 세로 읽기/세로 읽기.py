def solution(my_string, m, c):
    answer = ''
    for idx, val in enumerate(my_string):
        if idx % m == c-1:
            answer += val
    return answer