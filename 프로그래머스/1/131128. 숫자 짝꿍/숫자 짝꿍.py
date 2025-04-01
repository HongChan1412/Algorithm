def solution(X, Y):
    answer = ''
    count_chk = True
    for i in reversed(range(10)):
        x_count = X.count(str(i))
        y_count = Y.count(str(i))
        if x_count and y_count:
            count_chk = False
        else:
            continue
            
        if x_count >= y_count:
            answer += y_count*str(i)
        else:
            answer += x_count*str(i)
    if count_chk:
        answer = "-1"
    if answer[0] == "0":
        answer = "0"
    
    return answer
