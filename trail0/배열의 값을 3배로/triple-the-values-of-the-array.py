arr = [list(map(int, input().split())) for _ in range(3)]

for row in arr:
    for num in row:
        print(num*3, end =' ')
    print()
