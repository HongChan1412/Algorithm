def solution(n, words):
    answer = [0, 0]
    tmp = words[0]
    for i, word in enumerate(words):
        if i != 0:
            if (word[0] != tmp[-1]) or (word in words[:i]):
                if (i+1) % n == 0:
                    answer[0] = n
                else:
                    answer[0] = (i+1) % n
                answer[1] = i // n + 1
                break                
        tmp = word
    return answer