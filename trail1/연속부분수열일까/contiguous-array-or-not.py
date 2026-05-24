N1, N2 = map(int, input().split())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

lenB = len(B)
seqTF = 0
for i in range(len(A)-len(B)+1):
    if A[i:i+lenB] == B:
        seqTF = 1
        break
if seqTF == 1:
    print('Yes')
else:
    print('No')

