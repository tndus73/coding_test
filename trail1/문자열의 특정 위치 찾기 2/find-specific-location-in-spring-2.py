arr = ["apple", "banana", "grape", "blueberry", "orange"]

n = input()
cnt =0

for i in arr:
    if i[2]==n or i[3]==n:
        print(i)
        cnt += 1
print(cnt)