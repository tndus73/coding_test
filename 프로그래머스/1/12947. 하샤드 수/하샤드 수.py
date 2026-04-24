def solution(x):

    sumT = 0
    for i in str(x):
        sumT += int(i)
    if x % sumT == 0 :  
        return True
    return False