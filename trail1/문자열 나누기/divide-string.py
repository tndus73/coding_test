n = int(input())
strT  = ""

strT = ''.join(input().split())

for i in range(0, len(strT), 5):
    print(strT[i:i+5])