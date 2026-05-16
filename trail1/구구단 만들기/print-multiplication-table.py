A, B = map(int, input().split())

for i in range(1,10):
    for j in range(B,A-1,-2):
        print(f"{j} * {i} = {i*j}", end =' ')
        if j > A:
            print('/', end = ' ')
    print()