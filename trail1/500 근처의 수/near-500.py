N = list(map(int, input().split()))
A = 1
B = 1000

for i in N:
    if i > 500:
        B = min(i,B)
    elif i < 500:
        A = max(i,A)

print(A, B, end =' ')