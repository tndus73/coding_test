N = int(input())
cnt = 0

for i in range(N):
    for j in range(i):
        print(' ', end =' ')
    for j in range(N-i):
        print(chr(ord('A')+cnt), end =' ')
        cnt+=1
        if cnt == 26:
            cnt = 0
    print()