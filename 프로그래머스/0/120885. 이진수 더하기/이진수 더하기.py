def solution(bin1, bin2):
    answer = ''
    
    answer = format(int(bin1, 2) + int(bin2, 2), "b")
    
    return answer