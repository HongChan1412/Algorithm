def solution(arr):
    answer = []
    for i in range(0, 11):
        if len(arr) <= 2 ** i:
            answer = [0] * (2 ** i)
            break
    for idx, val in enumerate(arr):
        answer[idx] = val
    return answer