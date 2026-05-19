n = int(input())
total = []

class people:
    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight

for _ in range(n):
    n_i, h_i, w_i = input().split()
    total.append(people(n_i, int(h_i), int(w_i)))

total.sort(key = lambda x : (x.height, -x.weight))

for f in total:
    print(f.name, f.height, f.weight)
# Please write your code here.