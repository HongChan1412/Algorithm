def solution(arr, n):
    answer = []
    for idx, i in enumerate(arr):
        if len(arr) % 2 == 1:
            if idx % 2 == 0:
                answer.append(i+n)
            else:
                answer.append(i)
        else:
            if idx % 2 == 1:
                answer.append(i+n)
            else:
                answer.append(i)
    
    return answer