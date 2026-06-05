n = int(input())
arr = [tuple(map(int, input().split())) for _ in range(n)]

answer = 0

for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            listT = [0] *101
            
            for idx in range(n):
                if idx == i or idx == j or idx == k:
                    continue
                a, b = arr[idx]

                for x in range(a, b+1):
                    listT[x] += 1
            
            if max(listT) <= 1:
                answer += 1

print(answer)

