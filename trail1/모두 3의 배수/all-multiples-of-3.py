answer = 1

for _ in range(5):
    N = int(input())
    if N % 3 != 0:
        answer = 0
        break

if answer == 1:
    print(1)
else:
    print(0)