def solution(arr, queries):
    answer = []
    answer = arr
    for s, e in queries:
        answer = [val + 1 if s <= idx <= e else val for idx, val in enumerate(answer)]
        
    return answer