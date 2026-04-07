str = input()
str2 =''
for i in range(len(str)):
    if str[i].isupper():
        str2 += str[i].lower()
    else:
        str2 += str[i].upper()
print(str2)        
        