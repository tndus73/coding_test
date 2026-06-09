n = int(input())
ranges = [tuple(map(int, input().split())) for _ in range(n)]

arr = []

for x in range(1,10001):
    ok = True
    for a, b in ranges:
        x *= 2
        if x < a or x > b:
            ok = False
            break
    
    if ok:
        arr.append(x//(2**n))
print(min(arr))