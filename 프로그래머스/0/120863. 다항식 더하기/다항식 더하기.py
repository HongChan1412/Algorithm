def solution(polynomial):
    answer = ''
    polynomial = polynomial.split()
    
    polynomial_dict = {
        "x": 0,
        "int": 0
    }
    
    for i in polynomial:
        if "x" in i:
            if i == "x":
                polynomial_dict["x"] += 1
            else:
                polynomial_dict["x"] += int(i[:-1])
        elif "+" not in i:
            polynomial_dict["int"] += int(i)
    
    for k, v in polynomial_dict.items():
        if v != 0 and k == "x":
            if v != 1:
                answer += str(v)
            answer += "x"
        elif v != 0 and k == "int":
            if answer == "":
                answer = f"{v}"
            else:
                answer += f" + {v}"
        
    return answer