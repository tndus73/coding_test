n, m = map(int, input().split())

A = [0]
B = [0]
cur = 0

for _ in range(n):
    v, t = map(int, input().split())
    for _ in range(t):
        cur += v
        A.append(cur)
cur = 0
for _ in range(m):
    v, t = map(int, input().split())
    for _ in range(t):
        cur += v
        B.append(cur)

leader = []

for i in range(1, len(A)):
    if A[i] > B[i] :
        leader.append('A')
    elif A[i] < B[i] :
        leader.append('B')

answer = 0
for i in range(1, len(leader)):
    if leader[i] != leader[i-1]:
        answer +=1
print(answer)
# Please write your code here.