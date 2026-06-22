A = input()
cnt = 1
arr = []

for i in range(1,len(A)):  
    if A[i] == A[i-1] :
        cnt +=1
    else:
        arr.append(A[i-1]) 
        arr.append(str(cnt))
        cnt = 1

arr.append(A[-1]) 
arr.append(str(cnt))

print(len(''.join(arr)))
print(''.join(arr))