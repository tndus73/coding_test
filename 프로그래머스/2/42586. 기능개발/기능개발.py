def solution(progresses, speeds):
        day = []
        count = 1
        answer = []
        for i, j in zip(progresses, speeds):
            if (100-i) % j == 0:
                day.append((100-i) //j)
            else:
                day.append((100-i) //j +1)
        stand = day[0]        
        for k in range(1, len(day)):
            if stand >=  day[k]:
                count +=1    
            else:
                answer.append(count)
                count = 1
                stand = day[k]
        answer.append(count)        
        return answer