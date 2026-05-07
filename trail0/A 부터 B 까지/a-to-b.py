A, B = map(int, input().split())

while B>=A:
    print(A, end = ' ')
    if A %2 != 0:
        A = A*2
    else:
        A +=3