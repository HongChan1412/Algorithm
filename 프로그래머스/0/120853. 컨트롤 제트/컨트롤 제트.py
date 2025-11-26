def solution(s):
    answer = 0
    temp = 0
    s_split = s.split()
    for idx, i in enumerate(s_split):
        if i == "Z":
            answer -= int(s_split[idx-1])
        else:
            answer += int(i)
        
    return answer