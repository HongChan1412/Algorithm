def solution(quiz):
    answer = []
    for i in quiz:
        quiz_list = i.split()
        temp = quiz_list[0]
        if quiz_list[1] == "+":
            if int(quiz_list[0]) + int(quiz_list[2]) == int(quiz_list[4]):
                answer.append("O")
            else:
                answer.append("X")
        elif quiz_list[1] == "-":
            if int(quiz_list[0]) - int(quiz_list[2]) == int(quiz_list[4]):
                answer.append("O")
            else:
                answer.append("X")
        
    return answer