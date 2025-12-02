def solution(arr, query):
    answer = []
    answer = arr
    for idx, val in enumerate(query):
        if idx % 2 == 0:
            answer = answer[:val+1]
        else:
            answer = answer[val:]
    return answer