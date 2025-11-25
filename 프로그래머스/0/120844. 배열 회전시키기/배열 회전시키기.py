def solution(numbers, direction):
    answer = []
    answer = [0 for i in range(len(numbers))]
    for idx, num in enumerate(numbers):
        if direction == "right":
            if idx == len(numbers)-1:
                answer[0] = num
            else:
                answer[idx+1] = num
        elif direction == "left":
            if idx == 0:
                answer[-1] = num
            else:
                answer[idx-1] = num
    return answer