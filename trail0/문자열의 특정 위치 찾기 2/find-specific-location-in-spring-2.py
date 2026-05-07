text = str(input())
arr = ["apple", "banana", "grape", "blueberry", "orange"]
arr2 = []
for i in arr:
    if i[2] == text or i[3] == text:
        arr2.append(i)
for i in arr2:
    print(i)
print(len(arr2))