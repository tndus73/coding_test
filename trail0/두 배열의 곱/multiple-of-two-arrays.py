arr = [list(map(int, input().split())) for _ in range(3)]
input()
arr2 = [list(map(int, input().split())) for _ in range(3)]

answer = []

for i in range(3):
    row = []
    for j in range(3):
        row.append(arr[i][j] * arr2[i][j])
    answer.append(row)

for row in answer:
    print(*row)