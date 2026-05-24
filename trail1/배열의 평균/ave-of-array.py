nums = [list(map(int, input().split())) for _ in range(2)]

for rows in nums:
    print(sum(rows)/len(rows), end =' ')
print()

for i in range(len(nums[0])):
    CsumT = 0
    for rows in nums:
        CsumT += rows[i]
    print(CsumT/len(nums), end = ' ')
print()

total = 0
count = 0

for row in nums:
    total += sum(row)
    count += len(row)
print(f'{total/count:.1f}')