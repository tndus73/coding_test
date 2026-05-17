n = int(input())

def sum10():
    sumT = 0
    for i in range(1,n+1):
        sumT += i
    return sumT//10

result = sum10()
print(result)