def solution(array, n):
    answer = 0
    temp_abs = 100
    temp_num = 0
    for i in array:
        abs_i_n = abs(i-n)
        if abs_i_n <= temp_abs:
            if temp_abs == abs_i_n:
                if temp_num > i:
                    temp_num = i
            else:
                temp_num = i
            temp_abs = abs_i_n
                    
    answer = temp_num
    return answer