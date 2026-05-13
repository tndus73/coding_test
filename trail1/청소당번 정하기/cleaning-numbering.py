cntC = 0 
cntR = 0
cntB = 0

n = int(input())

for i in range(1, n+1):
    if i % 12 == 0:
        cntB += 1
    elif i % 3 == 0:
        cntR += 1
    elif i % 2 == 0:
        cntC +=1
print(cntC, cntR, cntB, end =' ')