'''
def solution(numbers, target):
    answer = 0
    def dfs(idx, total): #몇번째숫자인지, 지금까지만든합
        nonlocal answer #바깥변수 쓰겠다.
        
        #끝까지 왔을 때 종료조건
        if idx == len(numbers):
            if total == target:
                answer +=1
            return
        
        #+ 선택
        dfs(idx+1, total+numbers[idx])
        
        #- 선택
        dfs(idx+1, total-numbers[idx])
    dfs(0,0)
    return answer '''

def solution(numbers, target):

    def dfs(idx, total):
        #종료조건
        if idx == len(numbers):
            return 1 if total == target else 0
        #다음탐색
        return dfs(idx + 1, total + numbers[idx]) + dfs(idx + 1, total - numbers[idx])

    return dfs(0, 0)