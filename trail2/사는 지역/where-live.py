n = int(input())
total = []

class people:
    def __init__(self, name, street, region):
        self.name = name
        self.street = street
        self.region = region

for _ in range(n):
    n_i, s_i, r_i = input().split()
    total.append(people(n_i, s_i, r_i))

total.sort(key=lambda x : x.name, reverse=True)
P = total[0]

print(f'name {P.name}')
print(f'addr {P.street}')
print(f'city {P.region}')