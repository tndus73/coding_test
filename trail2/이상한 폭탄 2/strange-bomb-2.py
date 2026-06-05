N, K = map(int, input().split())
num = [int(input()) for _ in range(N)]

#폭탄의 개수 N, 특정거리 K,
#폭탄 나열한 순서가 주어지면, 폭발 할 폭탄 중 번호가 가장 큰 번호 출력

arr = []

for i in range(N):
    for j in range(i+1, N):
        if num[i] == num[j] and j-i<=K :
            arr.append(num[i])

if arr:
    print(max(arr))
else:
    print(-1)
