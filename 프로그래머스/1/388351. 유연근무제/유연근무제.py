def solution(schedules, timelogs, startday):
    answer = 0
    # 10:13 -> 1013
    # 09:58 -> 958
    # 출근인정시각 : +10
    # 1 -> 월
    # 2 -> 화
    # 3 -> 수
    # 4 -> 목
    # 5 -> 금
    # 6 -> 토
    # 7 -> 일
    
    # schedules
    # [700, 800, 1100]
    
    # timelogs
    # [[710, 2359, 1050, 700, 650, 631, 659], 
    # [800, 801, 805, 800, 759, 810, 809], 
    # [1105, 1001, 1002, 600, 1059, 1001, 1100]]
    
    # startday
    # 5
    
    # result
    # 3
    
    
    # 5금, 6토, 7일,
    # 8월, 9화, 10수, 11목, 12금, 13토, 14일
    # 15월
    # 금 토  일 월
    for schedule, timelog in zip(schedules, timelogs):
        is_ok = True
        for idx, val in enumerate(timelog):
            day = ((startday - 1) + idx) % 7 + 1
            
            if day % 6 != 0 and day % 7 != 0:
                schedule_hour = schedule // 100
                schedule_min = schedule % 100 + 10
                
                if schedule_min >= 60:
                    schedule_hour += 1
                    schedule_min %= 60
                
                if val > schedule_hour * 100 + schedule_min:
                    is_ok = False
                    break

        if is_ok:
            answer += 1
                
    return answer