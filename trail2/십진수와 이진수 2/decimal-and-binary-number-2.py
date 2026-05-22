N = input()
num = 0

for i in range(len(N)):
    num = num*2 + int(N[i])

num *= 17
arr = []

while True:
    if num < 1:
        break
    arr.append(num%2)
    num //= 2

for i in arr[::-1]:
    print(i, end ='')
# Please write your code here.