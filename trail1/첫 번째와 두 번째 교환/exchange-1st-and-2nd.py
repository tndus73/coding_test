alp = list(input())
a = alp[0]
b = alp[1]

for i in range(len(alp)):
    if alp[i] == a:
        alp[i] = b
    elif alp[i] == b:
        alp[i] = a
    
print(''.join(alp))