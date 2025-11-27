def solution(numbers, k):
    answer = 0
    answer = numbers[((k-1) * 2) % len(numbers)]
    return answer