n = int(input())
a = list(map(int, input().split()))

mina = a[0]

for i in range(1,len(a)):
    if a[i] < mina:
        mina = a[i]

cnt = 0

for i in a:
    if i == mina:
        cnt += 1

print(mina, cnt, end =' ')