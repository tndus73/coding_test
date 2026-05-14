N = int(input())
x = 0

while 2**x < N:
    x +=1 

if 2**x == N:
    print(x)