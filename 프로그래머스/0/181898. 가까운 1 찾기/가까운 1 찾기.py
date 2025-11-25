def solution(arr, idx):
    answer = 0
    temp = []
    for i in range(len(arr)):
        if arr[i] == 1 and i >= idx:
            temp.append(i)

    if temp:
        answer = min(temp)
    else:
        answer = -1
    return answer