n = int(input())
a = list(map(int, input().split()))

answer = 0
for k in range(201):
    cnt = 0
    for i in range(n):
        for j in range(i+1, n):
            if a[j]-k == k-a[i]:
                cnt+= 1
    answer = max(answer, cnt)
print(answer)