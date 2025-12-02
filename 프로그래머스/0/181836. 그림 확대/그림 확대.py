def solution(picture, k):
    answer = []
    for val1 in picture:
        s = ""
        for val2 in val1:
            s += val2 * k
        for _ in range(k):
            answer.append(s)

    
    return answer