def solution(M, N):
    answer = 0
    
    sero = M-1
    garo = (N-1) * M
    answer = sero + garo
    return answer