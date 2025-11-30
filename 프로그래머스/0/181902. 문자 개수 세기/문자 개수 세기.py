def solution(my_string):
    answer = []
    answer = [0 for i in range(52)]
    for i in my_string:
        if i <= "Z":
            answer[ord(i)-65] += 1
        else:
            answer[ord(i)-71] += 1

    return answer