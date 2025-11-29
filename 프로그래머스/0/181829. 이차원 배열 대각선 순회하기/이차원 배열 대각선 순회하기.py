def solution(board, k):
    answer = 0
    for idx1, val1 in enumerate(board):
        for idx2, val2 in enumerate(val1):
            if idx1+idx2 <= k:
                answer += board[idx1][idx2]
    return answer