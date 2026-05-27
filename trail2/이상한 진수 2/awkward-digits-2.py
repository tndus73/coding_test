a = list(input())

answer = 0

for i in range(len(a)):
    temp = a[:]

    if temp[i] == '0':
        temp[i] = '1'
    else:
        temp[i] = '0'
    
    num = int(''.join(temp),2)
    answer = max(answer, num)
print(answer)