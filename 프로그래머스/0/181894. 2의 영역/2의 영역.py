def solution(arr):
    answer = []
    index_2 = [idx for idx, val in enumerate(arr) if val == 2]
    # print(indexs)
    if len(index_2) == 1:
        answer = [2]
    elif len(index_2) > 1:
        answer = arr[index_2[0]:index_2[-1]+1]
    else:
        answer = [-1]
    return answer