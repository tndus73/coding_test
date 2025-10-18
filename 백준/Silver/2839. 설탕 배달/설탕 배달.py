N = int(input())
cnt = 0

while N >= 0:
    if N % 5 == 0:    #N이 5로 나눠떨어지는 경우
        cnt += N // 5
        print(cnt)
        break
    N -= 3 # 3kg봉투 한개씩 빼기
    cnt += 1
else:
    print(-1)

