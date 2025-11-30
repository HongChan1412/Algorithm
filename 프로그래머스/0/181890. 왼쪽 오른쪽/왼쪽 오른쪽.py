def solution(str_list):
    answer = []
    temp_index = 0 
    temp_str = ""
    for idx, val in enumerate(str_list):
        if val == "l" or val == "r":
            temp_index = idx
            temp_str = val
            break
            
    if temp_str == "l":
        answer = str_list[:temp_index]
    elif temp_str == "r":
        answer = str_list[temp_index+1:]
    return answer