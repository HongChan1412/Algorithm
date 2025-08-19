from functools import cmp_to_key

def solution(numbers):
    answer = ''
    numbers = list(map(str, numbers))
    
    # while numbers:
    #     high = numbers[0]
    #     for number in numbers[1:]:
    #         if high+number < number+high:
    #             high = number
    #     answer=answer + high
    #     numbers.remove(high)
    
    numbers.sort(key = cmp_to_key(lambda x, y: -1 if x+y > y+x else 1))
    answer = ''.join(numbers)
    answer = answer.lstrip('0') or '0'
    # print(answer)
    return answer