arr = list(map(int, input().split()))
newarr = []

for i in arr:
    newarr.append(i)
    if i == 0:
        newarr.pop()
        break

for i in newarr:
    if i % 2 != 0:
        print(i+3, end =' ')
    else:
        print(i//2, end =' ')