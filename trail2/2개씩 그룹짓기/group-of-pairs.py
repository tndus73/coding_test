N = int(input())
nums = list(map(int, input().split()))
nums.sort()
answer = 0

for i in range(N):
    answer2 = nums[i]+nums[2*N-1-i]
    answer = max(answer, answer2)

print(answer)

# Please write your code here.
