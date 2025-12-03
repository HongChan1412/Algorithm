def solution(n):
    answer = [[]]
    answer = [[0] * n for i in range(n)]
    dirs = [
        (0, 1), (1, 0), (0, -1), (-1, 0)
    ]
    num = 1
    
    nx, ny = 0, 0
    current_x, current_y = 0, 1

    for i in range(1, n**2+1):
        answer[nx][ny] = i
        
        if 0 <= nx+current_x <= n-1 and 0 <= ny+current_y <= n-1 and answer[nx+current_x][ny+current_y] == 0:
            nx = nx + current_x
            ny = ny + current_y
        else:
            for dx, dy in dirs:
                if 0 <= nx+dx <= n-1 and 0 <= ny+dy <= n-1 and answer[nx+dx][ny+dy] == 0:
                    nx = nx + dx
                    ny = ny + dy
                    current_x, current_y = dx, dy
                    break
    
    return answer