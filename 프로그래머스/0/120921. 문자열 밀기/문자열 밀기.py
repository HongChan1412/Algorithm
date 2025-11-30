def solution(A, B):
    answer = 0
    answer = -1
    A_list = []

    if A == B:
        answer = 0
    else:
        for i in range(1, len(A)+1):
            if B == A[-i:len(A)]+A[0:-i]:
                answer = i
                break
        
    return answer