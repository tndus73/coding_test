def solution(answers):
    answer = []
    A = [1,2,3,4,5]
    B = [2,1,2,3,2,4,2,5]
    C = [3,3,1,1,2,2,4,4,5,5]
    Acnt = 0
    Bcnt = 0
    Ccnt = 0
    for i in range(len(answers)):
        if A[i%len(A)] == answers[i]:
            Acnt +=1
        if B[i%len(B)] == answers[i]:
            Bcnt +=1
        if C[i%len(C)] == answers[i]:
            Ccnt +=1    
    if max(Acnt,Bcnt,Ccnt) == Acnt:
        answer.append(1)
    if  max(Acnt,Bcnt,Ccnt) == Bcnt:
        answer.append(2)   
    if max(Acnt,Bcnt,Ccnt) == Ccnt:
        answer.append(3)        
    return answer