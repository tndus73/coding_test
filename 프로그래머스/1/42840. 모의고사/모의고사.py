def solution(answers):
    A=0
    B=0
    C=0
    p1 = [1,2,3,4,5]
    p2 = [2,1,2,3,2,4,2,5]
    p3 = [3,3,1,1,2,2,4,4,5,5]
    for i in range(len(answers)):
        if answers[i] == p1[i%(len(p1))]:
            A+=1
        if answers[i] == p2[i%(len(p2))]:
            B+=1
        if answers[i] == p3[i%(len(p3))]:
            C+=1    
    answer = []
    if A == max(A,B,C):
        answer.append(1)
    if B == max(A,B,C):
        answer.append(2)
    if C == max(A,B,C):
        answer.append(3)    
    return answer