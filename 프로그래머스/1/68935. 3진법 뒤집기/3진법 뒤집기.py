'''
answer에 넣은건 3진법 후 반전된거
answer[::-1] 하면 일반 3진법

'''
def solution(n):
    answer = ''
    while n>0:
        answer += str(n%3)
        n = n // 3
    return int(answer,3)