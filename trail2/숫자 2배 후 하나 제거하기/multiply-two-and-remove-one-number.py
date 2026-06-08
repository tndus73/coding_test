n = int(input())
arr = list(map(int, input().split()))

answer = 10**18

for i in range(n):
    listT = arr[:]
    listT[i] *= 2

    for j in range(n):
        sumT = 0
        sumList = []
        for k in range(n):
            if j != k:
                sumList.append(listT[k])

        for k in range(n-2):
            sumT += abs(sumList[k+1] - sumList[k])

        answer = min(answer,sumT)
print(answer)