A = input()

answer = 0
for i in range(len(A)):
    for j in range(i+2, len(A)-1):
        if A[i]=='(' and A[i+1]=='(' and A[j]==')' and A[j+1]==')':
            answer +=1
print(answer)