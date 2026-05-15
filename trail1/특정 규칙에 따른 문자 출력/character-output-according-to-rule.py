N = int(input())

for i in range(N, 0 , -1):
    for j in range(i-1,0,-1):
        print(' ', end =' ')
    for j in range(i, N+1):
        print('@', end =' ')
    print()

for i in range(N-1, 0 , -1):
    for j in range(i,0,-1):
        print('@', end =' ')
    for j in range(i-1,0,-1):
        print(' ', end =' ')  
    print()