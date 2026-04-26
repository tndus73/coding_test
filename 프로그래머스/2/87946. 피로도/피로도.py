def solution(k, dungeons):
    visited = [False] * len(dungeons)
    
    def dfs(fatigue, visited):
        max_count = 0

        for i in range(len(dungeons)):
            if not visited[i]:
                need, cost = dungeons[i]
                
                if fatigue >= need:
                    visited[i] = True
                    count = 1+dfs(fatigue-cost, visited)
                    visited[i] = False
                    
                    max_count = max(max_count, count)
        return max_count                
    return dfs(k, visited)