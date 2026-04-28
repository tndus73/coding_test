def solution(answers):
    answer = []
    A = [1,2,3,4,5]
    B = [2,1,2,3,2,4,2,5]
    C = [3,3,1,1,2,2,4,4,5,5] 
    Acount = 0
    Bcount = 0
    Ccount = 0
    
    for i in range(len(answers)):
        if answers[i] == A[i%len(A)]:
            Acount += 1
        if answers[i] == B[i%len(B)]:
            Bcount += 1
        if answers[i] == C[i%len(C)]:
            Ccount += 1
    if max(Acount,Bcount,Ccount) == Acount:
        answer.append(1)
    if max(Acount,Bcount,Ccount) == Bcount:
        answer.append(2)
    if max(Acount,Bcount,Ccount) == Ccount:
        answer.append(3)
    return answer