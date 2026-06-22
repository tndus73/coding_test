word = input()
N = int(input())

for st in word[::-1][:N]:
    print(st,end='')