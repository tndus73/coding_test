A, B = map(int, input().split())

if A >= 90:
    if B >= 95:
        print(100000)
    elif B >= 90:
        print(50000)
    else:
        print(0)
else:
    print(0)