word, n = input().split()
word = list(word)

for _ in range(int(n)):
    k, a, b = input().split()
    if k == '1':
        a = int(a)
        b = int(b)
        word[a - 1], word[b - 1] = word[b - 1], word[a - 1]

    else:
        for i in range(len(word)):
            if word[i] == a:
                word[i] = b

    print(''.join(word))