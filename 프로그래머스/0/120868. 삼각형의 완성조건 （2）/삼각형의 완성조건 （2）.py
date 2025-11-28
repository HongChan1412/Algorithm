def solution(sides):
    answer = 0
    answer_list = []
    sides.sort()
    for i in range(1, sides[1]+1):
        if sides[1] < i + sides[0]:
            answer_list.append(i)
            
    for i in range(sides[1], sides[0]+sides[1]+1):
        if i < sides[0]+sides[1]:
            answer_list.append(i)

    answer = len(list(set(answer_list)))
    
    
    return answer