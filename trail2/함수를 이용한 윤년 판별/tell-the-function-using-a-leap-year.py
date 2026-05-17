y = int(input())

def is_TF(n):
    if n % 4 == 0:
        if n%100 == 0 and n%400 != 0 :
            return 'false'
        return 'true'
    else:
        return 'false'

print(is_TF(y))

# Please write your code here.