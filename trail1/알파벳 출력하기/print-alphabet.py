N = int(input())
cnt = 0

for i in range(1,N+1):
    for j in range(i):
        print(chr(ord('A')+cnt), end='')
        cnt +=1
        if cnt ==26:
            cnt = 0
    print()
