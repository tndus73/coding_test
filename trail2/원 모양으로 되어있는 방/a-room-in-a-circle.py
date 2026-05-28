n = int(input())

arr = [int(input()) for _ in range(n)]

answer = 10**18

for start in range(n):
    total = 0

    for room in range(n):
        dis = (room-start+n)%n
        total += dis * arr[room]
    
    answer = min(answer, total)
print(answer)