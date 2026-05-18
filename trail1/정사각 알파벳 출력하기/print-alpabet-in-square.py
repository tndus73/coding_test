N = int(input())
cnt = 0
for i in range(N):
    for _ in range(N):
        print(chr(ord('A')+cnt), end ='')
        cnt+=1
        if cnt == 27:
            cnt = 0
    print()