def solution(price):
    answer = 0
    answer = price
#     if price >= 500000:
#         answer *= 0.8
#     elif price >= 300000:
#         answer *= 0.9    
#     elif price >= 100000:
#         answer *= 0.95
    if price >= 100000 and price < 300000:
        answer *= 0.95
    elif price >= 300000 and price < 500000:
        answer *= 0.9
    elif price >= 500000:
        answer *= 0.8
    answer = int(answer)
    return answer