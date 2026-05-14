N = int(input())
answer = False

for i in range(2, N):
    if N % i == 0 :
        answer = True
        break
if answer == True:
    print('C')
else:
    print('N')
