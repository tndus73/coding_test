n = int(input())
students = [
    (h, w, i + 1)
    for i, (h, w) in enumerate([tuple(map(int, input().split())) for _ in range(n)])
]
students.sort(key=lambda x : (x[0], -x[1]))

for i in students:
    print(*i)

# Please write your code here.