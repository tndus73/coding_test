a, b = map(int, input().split())
n = input()
num = 0

for i in range(len(n)):
    num = num*a + int(n[i])

arr = []

while True:
    if num < 1 :
        break
    arr.append(num%b)
    num //= b

for i in arr[::-1]:
    print(i, end='')
# Please write your code here.