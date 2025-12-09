def solution(n, w, num):
    answer = 0
    boxes = [[-1] * w for i in range((n + w - 1) // w)]
    
    row = len(boxes)
    column = w
    nx, ny = 0, 0
    dirs = [
        (0, 1), # right
        (0, -1), # left
        (1, 0), # up
    ]
    c_dir = dirs[0]

    for i in range(1, n + 1):
        boxes[nx][ny] = i
        if i % w == 0:
            nx += 1
            if c_dir == dirs[0]:
                c_dir = dirs[1]
            elif c_dir == dirs[1]:
                c_dir = dirs[0]
        else:
            nx, ny = nx + c_dir[0], ny + c_dir[1]

    box_idx_nx = -1
    box_idx_ny = -1
        
    for idx, val in enumerate(boxes):
        if num in val:
            box_idx_nx = idx
            box_idx_ny = val.index(num)
            
        if box_idx_nx != -1:
            if val[box_idx_ny] != -1:
                answer += 1
                
    return answer