m1, d1, m2, d2 = map(int, input().split())
A = input()

days = [0,31,29,31,30,31,30,31,31,30,31,30,31]
days2 = ['Mon','Tue','Wed','Thu','Fri','Sat','Sun']

pri = sum(days[:m1])+d1
cur = sum(days[:m2])+d2

cnt = 0
for i in range(0, cur-pri+1):
    if A == days2[i%7]:
        cnt += 1

print(cnt)


# Please write your code here.