m1, d1, m2, d2 = map(int, input().split())

days = [0,31,28,31,30,31,30,31,31,30,31,30,31]
days2 = ['Mon','Tue','Wed','Thu','Fri','Sat','Sun']

# 1월 1일부터 m1월 d1일까지의 누적 일수
t1 = sum(days[:m1]) + d1
# 1월 1일부터 m2월 d2일까지의 누적 일수
t2 = sum(days[:m2]) + d2

# 두 날짜의 정확한 차이 (m2, d2가 항상 더 미래라고 가정)
cnt = t2 - t1

# m1월 d1일이 월요일(days2[0])이므로, 차이만큼 뒤로 밀어주면 됩니다.
print(days2[cnt % 7])
# Please write your code here.