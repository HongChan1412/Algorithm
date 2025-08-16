from collections import Counter

def solution(participant, completion):
    answer = ''
    counter_p = Counter(participant)
    counter_c = Counter(completion)
    # print(counter_p)
    # print(counter_c)
    # print(counter_p - counter_c)
    # print(list((counter_p - counter_c).keys())[0])
    answer = list((counter_p - counter_c).keys())[0]
    return answer