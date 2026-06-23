words, word = input().split()

if words.find(word) == -1:
    print('No')
else:
    print(words.find(word))