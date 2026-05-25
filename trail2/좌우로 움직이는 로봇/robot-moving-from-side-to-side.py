n, m = map(int, input().split())

A = [0]
B = [0]
cur = 0

for _ in range(n):
    time, direction = input().split()
    time = int(time)
    for _ in range(time):
        if direction == 'R':
            cur += 1
            A.append(cur)
        else:
            cur -= 1
            A.append(cur)

cur = 0
for _ in range(m):
    time, direction = input().split()
    time = int(time)
    for _ in range(time):
        if direction == 'R':
            cur += 1
            B.append(cur)
        else:
            cur -= 1
            B.append(cur)

max_len = max(len(A),len(B))
while len(A) < max_len:
        A.append(A[-1])
while len(B) < max_len:
        B.append(B[-1])

cnt = 0
for i in range(1, max_len):
    if A[i-1] != B[i-1] and A[i] == B[i]:
        cnt += 1
print(cnt)