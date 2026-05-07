count1=0
count2=0
for _ in range(10):
    n=int(input())
    if(n%3==0):
        count1+=1
    if(n%5==0):
        count2+=1

print(count1, count2)
