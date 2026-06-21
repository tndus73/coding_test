N = int(input())

strlen = 0
cnt = 0

for _ in range(N):
    alp = input()
    if alp[:1] =='a':
        cnt +=1
    strlen += len(alp)

print(strlen, cnt, end =' ')