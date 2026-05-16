N = int(input())

for i in range(1,N+1):
    for j in range(N*i, i-1, -i):
        print(j, end =' ')
    print()