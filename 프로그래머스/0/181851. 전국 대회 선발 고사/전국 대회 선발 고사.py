def solution(rank, attendance):
    answer = 0
    temp = []
    for i, j in zip(rank, attendance):
        if j:
            temp.append(i)
    temp.sort()
    answer = 10000 * rank.index(temp[0]) + 100 * rank.index(temp[1]) + rank.index(temp[2])
    return answer