n = int(input())
a = list(map(int, input().split()))

k = sorted(a, reverse = True)

print(k[0], k[1], end =' ')