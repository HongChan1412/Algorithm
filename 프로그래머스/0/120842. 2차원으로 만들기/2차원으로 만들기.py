def solution(num_list, n):
    answer = [[]]
    answer = [[0] * n for i in range(int(len(num_list) / n))]
    
    for idx, i in enumerate(num_list):
        answer[idx // n][idx % n] = i
    
    return answer