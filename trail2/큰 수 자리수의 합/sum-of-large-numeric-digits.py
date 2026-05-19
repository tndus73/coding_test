a, b, c = map(int, input().split())

def sum3(a, b, c):
    mul = a*b*c
    sumT = 0
    for i in str(mul):
        sumT += int(i)
    return sumT

print(sum3(a,b,c))


# Please write your code here.