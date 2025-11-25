from collections import Counter
def solution(array, n):
    answer = 0
    cnt = Counter(array)
    answer = cnt[n]
    return answer