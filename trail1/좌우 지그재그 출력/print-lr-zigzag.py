N = int(input())

for i in range(N):
    start = i*N + 1

    if i % 2 == 0:
        for j in range(start, start+N):
            print(j, end= ' ')
    else:
        for j in range(start+N-1, start-1, -1):
            print(j, end= ' ')
    print()