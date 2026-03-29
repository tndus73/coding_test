def solution(k, dungeons):
    
    def dfs(k, visited):
        max_count = 0

        for i in range(len(dungeons)):
            if not visited[i] and k >= dungeons[i][0]:
                visited[i] = True
                count = 1 + dfs(k - dungeons[i][1], visited)
                max_count = max(max_count, count)
                visited[i] = False

        return max_count

    visited = [False] * len(dungeons)
    return dfs(k, visited)