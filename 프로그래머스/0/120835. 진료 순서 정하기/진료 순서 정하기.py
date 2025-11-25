def solution(emergency):
    answer = []
    emergency_list = sorted(emergency, reverse=True)
    
    for i in emergency:
        answer.append(emergency_list.index(i)+1)
    return answer