def solution(num_list):
    answer = []
    num_list.sort()
    for i in range(5):
        del num_list[0]
    answer = num_list
    return answer