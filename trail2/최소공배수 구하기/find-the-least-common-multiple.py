n, m = map(int, input().split())

def lcm(n,m):
    for i in range(min(n,m), n*m+1):
        if i % n == 0 and i % m == 0:
            print(i)
            break

lcm(n,m)
# Please write your code here.