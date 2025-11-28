def solution(my_str, n):
    answer = []
    answer = [""]
    temp = 0
    for idx, i in enumerate(my_str):
        if len(answer[temp]) <= n:
            answer[temp] += i
        if len(answer[temp]) == n and idx != len(my_str)-1:
            answer.append("")
            temp += 1
            
    return answer