def solution(id_pw, db):
    answer = ''
    answer = "fail"
    for id, pw in db:
        if id == id_pw[0]:
            answer = "wrong pw"
            if pw == id_pw[1]:
                answer = "login"
                break
    return answer