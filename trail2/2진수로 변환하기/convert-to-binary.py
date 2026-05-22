n = int(input())
arr = []

while True:
    arr.append(n % 2)
    n //= 2
    if n < 1:
        break

for i in arr[::-1]:
    print(i, end ='')
# Please write your code here.