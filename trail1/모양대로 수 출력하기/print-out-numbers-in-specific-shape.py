N = int(input())

for i in range(N,0,-1):
    for j in range(N-i):
        print(' ', end =' ')
    for j in range(i,0,-1):
        print(j, end =' ')
    print()
