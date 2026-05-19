n = int(input())
total = []

class forcast:
    def __init__(self, date, day, weather):
        self.date = date
        self.day = day
        self.weather = weather 

for _ in range(n):
    d, dy, w = input().split()
    total.append(forcast(d, dy, w))

rain = []
for f in total:
    if f.weather == 'Rain':
        rain.append(f)

rain.sort(key=lambda x : x.date)
print(rain[0].date, rain[0].day, rain[0].weather, end =' ')

# Please write your code here.