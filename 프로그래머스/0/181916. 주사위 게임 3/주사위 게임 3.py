from collections import Counter
def solution(a, b, c, d):
    answer = 0
    cnt = Counter([a, b, c, d])
    
    if len(cnt) == 1:
        answer = 1111 * a    
    elif 3 in cnt.values():
        p = [k for k, v in cnt.items() if v == 3][0]
        q = [k for k, v in cnt.items() if v == 1][0]
        answer = (10 * p + q) ** 2
    elif len(cnt) == 2:
        temp = sorted(list(set([a, b, c, d])), reverse=True)
        answer = (temp[0]+temp[1]) * abs(temp[0]-temp[1])
    elif len(cnt) == 3:
        q, r = [k for k, v in cnt.items() if v == 1]
        answer = q * r
    else:
        answer = min([a, b, c, d])
        
    return answer