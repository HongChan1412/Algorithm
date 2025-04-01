from itertools import combinations

def check_sosu(num: int):
    if (num % 2 == 0) or (num % 3 == 0) or (num % 5 == 0):
        return False
    for i in range(7, num+1):
        if i == num:
            return True
        if num % i == 0:
            return False
    


def solution(nums):
    answer = 0
    answers = []
    combies = list(combinations(nums, 3))
    for combi in combies:
        res = sum(combi)
        if check_sosu(res):
            answers.append(res)
    answer = len(answers)
    return answer