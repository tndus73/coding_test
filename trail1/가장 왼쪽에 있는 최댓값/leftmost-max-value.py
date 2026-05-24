n = int(input())
a = list(map(int, input().split()))

point = n

while True:
    max_idx = 0
    for i in range(point):
        if a[i] > a[max_idx]:
            max_idx = i
    
    point = max_idx
    print(max_idx+1, end =' ')
    
    if max_idx == 0:
        break