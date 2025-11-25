def solution(num_list):
    answer = 0
    Gob = 1
    Hab = 0
    for i in num_list:
        Gob = Gob * i
        Hab = Hab + i
    
    if Hab ** 2 > Gob:
        answer = 1
    else:
        answer = 0
    return answer