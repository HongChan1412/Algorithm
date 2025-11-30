def solution(score):
    answer = []
    score = [x+y for x, y in score]
    score_sort = sorted(score, reverse=True)
    
    for i in score:
        answer.append(score_sort.index(i)+1)
    return answer