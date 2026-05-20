N = int(input())
arr = list(map(int, input().split()))
arrCnt = [0] * 9

for i in arr:
    arrCnt[i-1] += 1

for j in arrCnt:
    print(j)