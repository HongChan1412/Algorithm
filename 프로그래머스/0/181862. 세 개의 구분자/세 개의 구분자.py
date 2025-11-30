import re
def solution(myStr):
    answer = []
    answer = re.sub(r"[a, b, c]", " ", myStr)
    answer = answer.split()
    if answer == []:
        answer = ["EMPTY"]
    return answer