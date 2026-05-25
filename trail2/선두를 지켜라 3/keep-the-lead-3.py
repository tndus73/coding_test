N, M = map(int, input().split())

cur = 0
A = []
for _ in range(N):
    v, t = map(int, input().split())
    for _ in range(t):
        cur += v
        A.append(cur)

cur = 0
B = []
for _ in range(M):
    v, t = map(int, input().split())
    for _ in range(t):
        cur += v
        B.append(cur)

result = []
answer = 1

for i in range(len(A)):
    if A[i] > B[i]:
        result.append('A')
    elif A[i] < B[i]:
        result.append('B')
    else:
        result.append('C')

for i in range(1,len(result)):
    if result[i-1] != result[i]:
        answer += 1

print(answer) 