'''
개발속도는 다르지만, 배포는 앞에있는 기능 배포될때 뒤에 있는 기능 배포
먼저 배포되는 순서대로 작업 진도 정수배열 progresses
각 작업의 개발 속도 정수배열 speeds
각 배포마다 몇개의 기능이 배포되는지 return
import math

def solution(progresses, speeds):
    days = []
    
    for pro, spe in zip(progresses, speeds):
            days.append(math.ceil((100-pro)/spe))
            
    answer = []
    current = days[0]
    count = 1
    
    for i in range(1, len(days)):
        if days[i] <= current:
            count +=1
        else:
            answer.append(count)
            current = days[i]
            count = 1
            
    answer.append(count)
    return answer
'''
def solution(progresses, speeds):
        answer = []
        days=[]
    
        for p, s in zip(progresses, speeds):
            day = (100-p+s-1)//s
            days.append(day)
            
        current = days[0]
        count=1    
        
        for i in range(1, len(days)):
            if days[i] <= current:
                    count +=1
            else:
                    answer.append(count)
                    current = days[i]
                    count = 1
        answer.append(count)
        return answer