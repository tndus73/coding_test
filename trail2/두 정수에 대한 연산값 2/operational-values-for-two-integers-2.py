a, b = map(int, input().split())

def minmax(a, b):
    if a < b:
        a += 10
        b *= 2
    else:
        b += 10
        a *= 2
    return a, b

a, b = minmax(a,b)
print(a, b, end= ' ')
# Please write your code here.