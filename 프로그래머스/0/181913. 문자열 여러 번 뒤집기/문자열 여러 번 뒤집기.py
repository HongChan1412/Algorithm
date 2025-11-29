def solution(my_string, queries):
    answer = ''
    for i in queries:
        start = i[0]
        end = i[1]
        my_string = my_string[:start] + my_string[start:end+1][::-1] + my_string[end+1:]
    answer = my_string
    return answer