numlist = []
result =[]

for i in range(10):
    num = int(input())
    numlist.append(num)
    
for i in numlist:
    a = i%42
    if a not in result:
        result.append(a)
    else:
        continue

print(len(result))
    