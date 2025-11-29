def solution(arr):
    answer = 0
    answer = 1
    for idx1, val1 in enumerate(arr):
        for idx2, val2 in enumerate(val1):
            if arr[idx1][idx2] != arr[idx2][idx1]:
                answer = 0

    return answer