def solution(s):
    answer = len(s)

    for size in range(1, len(s)//2 + 1):
        prev = s[:size]   # 첫 덩어리
        count = 1
        compressed = ""

        for i in range(size, len(s), size):
            current = s[i:i+size]

            if prev == current:
                count += 1
            else:
                if count > 1:
                    compressed += str(count)
                compressed += prev

                prev = current
                count = 1

        # 마지막 처리
        if count > 1:
            compressed += str(count)
        compressed += prev

        answer = min(answer, len(compressed))

    return answer