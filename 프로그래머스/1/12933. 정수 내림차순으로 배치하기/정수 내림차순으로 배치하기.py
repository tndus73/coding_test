def solution(n):
    k = []
    answer =''
    for i in str(n):
        k += i
    k.sort(reverse=True)   
    for i in k:
        answer += i
    return int(answer)