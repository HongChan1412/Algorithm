from collections import Counter
def solution(lines):
    answer = 0
    gyeopchim = []
    for start, end in lines:
        for i in range(start, end, 1):
            middle = (i + 1) / 2
            gyeopchim.append(middle)
            
    for k, v in Counter(gyeopchim).items():
        if v >= 2:
            answer += 1
    return answer