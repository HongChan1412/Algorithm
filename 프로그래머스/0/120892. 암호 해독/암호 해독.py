def solution(cipher, code):
    answer = ''
    
    for idx, i in enumerate(cipher):
        if (idx+1) % code == 0:
            answer += i
    return answer