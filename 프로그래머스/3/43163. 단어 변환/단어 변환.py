from collections import deque

def solution(begin, target, words):
    def diff_one(a, b):
        count = 0
        for i in range(len(a)):
            if a[i] != b[i]:
                count += 1
        return count == 1

    if target not in words:
        return 0

    queue = deque()
    queue.append((begin, 0))
    visited = [False] * len(words)

    while queue:
        current, count = queue.popleft()

        if current == target:
            return count

        for i in range(len(words)):
            if not visited[i] and diff_one(current, words[i]):
                visited[i] = True
                queue.append((words[i], count + 1))

    return 0