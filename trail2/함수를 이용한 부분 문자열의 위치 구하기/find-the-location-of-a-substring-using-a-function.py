text = input()
pattern = input()

def point():
    N= len(text)
    M = len(pattern)
    for i in range(N-M+1):
        if text[i:i+M] == pattern:
            return i
    return -1

result = point()
print(result) 
# Please write your code here.