N = int(input())

for i in range(11, 11+(2*N-1),2):
    for j in range(i, i+2*N, 2):
        print(j, end =' ')
    print()