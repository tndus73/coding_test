N = int(input())
arr = list(map(float,input().split()))
print(round(sum(arr)/N,1))
if sum(arr)/N >= 4:
    print('Perfect')
elif sum(arr)/N >= 3:
    print('Good')
else:
    print('Poor')