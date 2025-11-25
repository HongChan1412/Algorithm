def solution(a, d, included):
    answer = 0
    
    for idx, i in enumerate(included):
        if i:
            answer = answer + idx*d + a
            print(idx*d+3)
            
    return answer