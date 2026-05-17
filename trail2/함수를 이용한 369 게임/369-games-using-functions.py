a, b = map(int, input().split())

def TF369(n):
    return '3' in str(n) or '6' in str(n) or '9' in str(n)

def TF3(n):
    return n % 3== 0 

cnt = 0

for i in range(a, b+1):
    if TF369(i) or TF3(i):
        cnt +=1
print(cnt)
# Please write your code here.