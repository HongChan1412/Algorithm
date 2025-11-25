def solution(my_string):
    answer = ''
    for i in my_string:
        if i >= "a" and i <= "z":
            answer += i.upper()
        elif i >= "A" and i <= "Z":
            answer += i.lower()
    return answer