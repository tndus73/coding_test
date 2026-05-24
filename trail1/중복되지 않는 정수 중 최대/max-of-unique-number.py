n = int(input())
nums = list(map(int, input().split()))

arr = [0] * 1001

for i in nums:
    arr[i] += 1

answer = -1

for i in range(1, len(arr)):
    if arr[i] == 1:
            answer = i
print(answer)