N = int(input())
answer = []
cnt = 0
sumT = 0

for _ in range(N):
    k = input()
    answer.append(k)

alp = input()

for stri in answer:
    if stri[0] == alp:
        cnt += 1
        sumT += len(stri)

print(cnt, f'{sumT/cnt:.2f}')

