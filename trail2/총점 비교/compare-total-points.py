n = int(input())

total = []

class student:
    def __init__(self, name, score1, score2, score3):
        self.name = name
        self.score1 = score1
        self.score2 = score2
        self.score3 = score3

for _ in range(n):
    name, score1, score2, score3 = input().split()
    total.append(student(name, int(score1), int(score2), int(score3)))

total.sort(key=lambda x : x.score1 + x.score2 + x.score3)

for f in total:
    print(f.name, f.score1, f.score2, f.score3 )
# Please write your code here.