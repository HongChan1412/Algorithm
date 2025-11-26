def solution(s):
    answer = ''
    alp = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    temp = []
    for i in alp:
        if s.count(i) == 1:
            temp.append(i)
    temp.sort()
    answer = "".join(temp)
    return answer