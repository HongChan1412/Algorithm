def solution(babbling):
    answer = 0
    joka = ["aya", "ye", "woo", "ma"]
    for i in babbling:
        joka_count = 0
        for j in joka:
            if j in i:
                joka_count += len(j)
        if joka_count == len(i):
            answer += 1
    return answer