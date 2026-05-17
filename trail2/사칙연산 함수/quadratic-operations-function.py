a, o, c = input().split()
a = int(a)
c = int(c)

def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    return a//b

if o == '+':
    print(f'{a} + {c} = {add(a,c)}')
elif o == '-':
    print(f'{a} - {c} = {sub(a,c)}')
elif o == '*':
    print(f'{a} * {c} = {mul(a,c)}')
elif o == '/':
    print(f'{a} / {c} = {div(a,c)}')
else:
    print('False')