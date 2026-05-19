n = 5

total = []

class people:
    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight

for _ in range(n):
    n, h, w = input().split()
    total.append(people(n,int(h),float(w)))

namesort = sorted(total, key=lambda x : x.name)
heightsort = sorted(total, key=lambda x : -x.height)

print('name')
for f in namesort:
    print(f.name, f.height, f.weight)

print()
print('height')
for f in heightsort:
    print(f.name, f.height, f.weight)

# Please write your code here.