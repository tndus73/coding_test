listT = []
answer = []
for _ in range(10):
    strT = input()
    listT.append(strT)
N = input()

for i in listT:
    if i[len(i)-1] == N:
        answer.append(i)

if answer:
    for i in answer:
        print(i)
else:
    print('None')