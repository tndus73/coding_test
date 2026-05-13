N = int(input())
sumT = 0

for i in range(1, 101):
    sumT += i
    if  sumT >=N :
        print(i)
        break
