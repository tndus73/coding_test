'''
def solution(ineq, eq, n, m):
    if eq == "!" :
        if ineq == "<" :
             return int(n<m) #1
        else:
            return int(n>m)
    else:
        if ineq == "<" :
             return int(n<=m)
        else:
            return int(n>=m)
'''
def solution(ineq, eq, n, m):
    answer = 0
    if ineq == ">" and eq == "=":
        if n >= m :
            answer = 1
        else :
            answer = 0
    elif ineq == "<" and eq == "=":
        if n <= m :
            answer = 1
        else :
            answer = 0
    elif ineq == ">" and eq == "!":
        if n > m :
            answer = 1
        else :
            answer = 0
    elif ineq == "<" and eq == "!":
        if n < m :
            answer = 1
        else :
            answer = 0 
    return answer