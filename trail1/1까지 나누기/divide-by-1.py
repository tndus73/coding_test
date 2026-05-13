N = int(input())
cnt = 0

for i in range(1, N):
    N //= i
    cnt += 1
    if N <= 1:
        break
print(cnt)
        

