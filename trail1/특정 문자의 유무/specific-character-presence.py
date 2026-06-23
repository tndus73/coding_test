word = input()

A = False
B = False
for i in range(len(word)-1):
    if word[i:i+2] == 'ee':
        A = True

    if word[i:i+2] == 'ab':
        B = True
if A:
    print('Yes', end =' ')
else: 
    print('No', end =' ')

if B:
    print('Yes', end ='')
else:
    print('No', end ='')