def solution(strArr):
    answer = 0
    arr = [0 for i in range(30)]
    for i in strArr:
        arr[len(i)-1] += 1
    answer = max(arr)
    return answer