N = int(input())
num = 1

for i in range(1,N+1):
    for _ in range(i):
        print(num, end =' ')
        num +=1
    print()