def solution(arr):
    answer = 0
    temp_arr = []
    while True:
        temp_arr = arr.copy()
        for idx, val in enumerate(arr):
            if val >= 50 and val % 2 == 0:
                arr[idx] = int(val / 2)
            elif val < 50 and val % 2 == 1:
                arr[idx] = val * 2 + 1
            else:
                arr[idx] = val

        if temp_arr == arr:
            break
        else:
            answer += 1
    return answer