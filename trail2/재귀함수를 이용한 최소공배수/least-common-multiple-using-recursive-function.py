n = int(input())
arr = list(map(int, input().split()))

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a%b)

def lcm(a, b):
    return a*b // gcd(a,b)

def find_lcm(idx):
    # 마지막 원소
    if idx == 0:
        return arr[0]
    return lcm(find_lcm(idx - 1), arr[idx])


print(find_lcm(n - 1))
# Please write your code here.