n = int(input())
total = []

class students:
    def __init__(self, name, korean, english , math):
        self.name = name
        self.korean = korean
        self.english = english
        self.math = math

for _ in range(n):
    si = input().split()
    total.append(students(si[0], int(si[1]), int(si[2]), int(si[3])))
total.sort(key=lambda x : (-x.korean, -x.english, -x.math))

for f in total:
    print(f.name, f.korean, f.english, f.math)

# Please write your code here.