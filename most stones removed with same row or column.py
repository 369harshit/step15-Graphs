from collections import defaultdict
class Solution:
    def removeStones(self, stones):
        rows = defaultdict(list)
        cols = defaultdict(list)

        for i, (x, y) in enumerate(stones):
            rows[x].append(i)
            cols[y].append(i)

        visited = set()
        components = 0

        def dfs(node):
            visited.add(node)
            for neighbor in rows[stones[node][0]] + cols[stones[node][1]]:
                if neighbor not in visited:
                    dfs(neighbor)

        for i in range(len(stones)):
            if i not in visited:
                components += 1
                dfs(i)

        return len(stones) - components

# Example usage:
stones = [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]
solution = Solution()
result = solution.removeStones(stones)
print("Maximum number of stones that can be removed:",result)
