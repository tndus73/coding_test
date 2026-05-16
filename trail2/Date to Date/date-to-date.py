m1, d1, m2, d2 = map(int, input().split())
answer = 0
days = [0,31,28,31,30,31,30,31,31,30,31,30,31]

if m1 == m2:
    answer += d2-d1+1
else:
    answer += days[m1] -d1 +1
    for i in range(m1+1,m2):
        answer += days[i]
    answer += d2

print(answer)
# Please write your code here.
