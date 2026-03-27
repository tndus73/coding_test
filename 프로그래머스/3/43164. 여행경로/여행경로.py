def solution(tickets):
    tickets.sort()
    used = [False] * len(tickets)
    path = ["ICN"]

    def dfs(now, count):
        if count == len(tickets):
            return True

        for i in range(len(tickets)):
            start, end = tickets[i]

            if not used[i] and start == now:
                used[i] = True
                path.append(end)

                if dfs(end, count + 1):
                    return True

                path.pop()
                used[i] = False

        return False

    dfs("ICN", 0)
    return path