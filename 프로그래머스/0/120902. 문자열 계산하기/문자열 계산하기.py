def solution(my_string):
    answer = 0
    my_string_list = my_string.split()
    answer = int(my_string_list.pop(0))
    
    for i in range(1, len(my_string_list)):
        if my_string_list[i-1] == "+":
            answer += int(my_string_list[i])
        elif my_string_list[i-1] == "-":
            answer -= int(my_string_list[i])

    return answer