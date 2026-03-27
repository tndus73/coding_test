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
        if idx == len(numbers):
            if total == target:
                return 1
            else:
                return 0

        plus_case = dfs(idx + 1, total + numbers[idx])
        minus_case = dfs(idx + 1, total - numbers[idx])

        return plus_case + minus_case

    return dfs(0, 0)