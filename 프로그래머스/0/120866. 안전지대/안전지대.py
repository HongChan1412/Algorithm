def solution(board):
    answer = 0

    if board == [[0]]:
        answer = 1
    elif board == [[1]]:
        answer = 0
    else:
        
    
        for idx1, val1 in enumerate(board):
            for idx2, val2 in enumerate(val1):
                if val2 == 0:
                    if idx1 == 0:
                        if idx2 == 0:
                            if board[idx1+1][idx2] or board[idx1][idx2+1] or board[idx1+1][idx2+1]:
                                continue
                        elif idx2 > 0 and idx2 < len(board)-1:
                            if board[idx1][idx2-1] or board[idx1+1][idx2-1] or board[idx1+1][idx2] or board[idx1][idx2+1] or board[idx1+1][idx2+1]:
                                continue                        
                        elif idx2 == len(board)-1:
                            if board[idx1][idx2-1] or board[idx1+1][idx2-1] or board[idx1+1][idx2]:
                                continue
                    elif idx1 > 0 and idx1 < len(board)-1:
                        if idx2 == 0:
                            if board[idx1-1][idx2] or board[idx1+1][idx2] or board[idx1-1][idx2+1] or board[idx1][idx2+1] or board[idx1+1][idx2+1]:
                                continue
                        elif idx2 > 0 and idx2 < len(board)-1:
                            if board[idx1-1][idx2-1] or board[idx1][idx2-1] or board[idx1+1][idx2-1] or board[idx1-1][idx2] or board[idx1+1][idx2] or board[idx1-1][idx2+1] or board[idx1][idx2+1] or board[idx1+1][idx2+1]:
                                continue
                        elif idx2 == len(board)-1:
                            if board[idx1-1][idx2-1] or board[idx1][idx2-1] or board[idx1+1][idx2-1] or board[idx1-1][idx2] or board[idx1+1][idx2]:
                                continue
                    elif idx1 == len(board)-1:
                        if idx2 == 0:
                            if board[idx1-1][idx2] or board[idx1-1][idx2+1] or board[idx1][idx2+1]:
                                continue
                        elif idx2 > 0 and idx2 < len(board)-1:
                            if board[idx1-1][idx2-1] or board[idx1][idx2-1] or board[idx1-1][idx2] or board[idx1-1][idx2+1] or board[idx1][idx2+1]:
                                continue
                        elif idx2 == len(board)-1:
                            if board[idx1-1][idx2-1] or board[idx1][idx2-1] or board[idx1-1][idx2]:
                                continue
                    answer += 1

    return answer