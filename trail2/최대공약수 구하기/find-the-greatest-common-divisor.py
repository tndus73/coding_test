n, m = map(int, input().split())

def gcd(n,m):
    arr = []
    for i in range(1, min(n,m)+1):
        if n % i == 0 and m % i == 0:
            arr.append(i)
    print(max(arr))

gcd(n,m)
# Please write your code here.