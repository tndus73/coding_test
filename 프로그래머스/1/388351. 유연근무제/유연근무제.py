def solution(schedules, timelogs, startday):
    answer = 0
    for i in range(len(schedules)):
        hope = schedules[i]
        hope = (hope//100)*60 + (hope%100)
        
        ok = True
        
        for j in range(7):
            day = (startday +j -1) % 7
            if day ==5 or day==6:
                continue
            real = timelogs[i][j]
            real = (real//100)*60 + (real%100)
            
            if real > hope + 10:
                ok = False
                break
        if ok:
             answer +=1
    return answer