Tlist = []


for _ in range(5):
    arr = list(input().split())
    Tlist.append(arr)

for row in Tlist:
    for i in row:
        print(i.upper(), end =' ')
    print()
    
