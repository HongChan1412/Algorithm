def solution(dots):
    answer = 0
    x_list = [x[0] for x in dots]
    y_list = [y[1] for y in dots]
    answer = (max(x_list) - min(x_list)) * (max(y_list) - min(y_list))
    
    
    return answer