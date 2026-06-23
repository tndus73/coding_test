cnt1 = 0
cnt2 = 0

strT = input()

for i in range(len(strT) - 1):
    if strT[i:i+2] == 'ee':
        cnt1 += 1

    if strT[i:i+2] == 'eb':
        cnt2 += 1

print(cnt1, cnt2)