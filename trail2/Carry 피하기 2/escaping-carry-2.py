n = int(input())
arr = [int(input()) for _ in range(n)]

answer = -1
for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            x, y, z = arr[i], arr[j], arr[k]
            ok = True
            while x > 0 or y > 0 or z > 0:
                if  x%10 + y%10 + z%10 >= 10:
                    ok = False
                    break

                x //= 10
                y //= 10
                z //= 10

            if ok:
                answer = max(answer, arr[i] + arr[j] + arr[k])

print(answer)