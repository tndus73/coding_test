text = str(input())
arr = ["apple", "banana", "grape", "blueberry", "orange"]
count = 0
for i in arr:
    if i[2] == text or i[3] == text:
        print(i)
        count +=1
print(count)