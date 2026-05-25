N, K, P, T = map(int, input().split())
handshakes = [tuple(map(int, input().split())) for _ in range(T)]

hand_sort = sorted(handshakes, key =lambda x : x[0])
people = [0]*(N+1)
people[P] = 1
cnt = [0] * (N+1)

for t, x, y in hand_sort:
    x_was = people[x]
    y_was = people[y]

    if x_was==1 and cnt[x] < K:
        people[y] = 1
        cnt[x] += 1
    if y_was==1 and cnt[y] < K:
        people[x] = 1
        cnt[y] += 1

print(*people[1:], sep='')
