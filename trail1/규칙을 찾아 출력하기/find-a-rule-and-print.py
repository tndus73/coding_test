N = int(input())

for i in range(N):
    for j in range(N):
        if i==0 or i==N-1 :
            print('*', end =' ')
        else:
            if j <= i-1 or j==N-1:
                print('*', end =' ')
            else:
                print(' ', end =' ')
    print()