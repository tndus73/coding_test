N = int(input())
str = input()

for length in range(1, N+1):
    count = {}

    for start in range(N-length+1):
        sub = str[start:start+length]

        if sub not in count:
            count[sub] = 0

        count[sub] += 1
    
    ok = True

    for sub in count:
        if count[sub] >= 2:
            ok = False
            break
    
    if ok:
        print(length)
        break