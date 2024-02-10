from collections import defaultdict
def accountsMerge(accounts):
    graph = defaultdict(list)
    
    for account in accounts:
        for i in range(2, len(account)):
            graph[account[i]].append(account[i - 1])
            graph[account[i - 1]].append(account[i])

    visited = set()
    result = []

    def dfs(email, component):
        if email not in visited:
            visited.add(email)
            component.append(email)
            for neighbor in graph[email]:
                dfs(neighbor, component)

    for account in accounts:
        name = account[0]
        email = account[1]
        component = []

        if email not in visited:
            dfs(email, component)
            result.append([name] + sorted(component))

    return result

# Example usage:
accounts = [["John", "johnsmith@mail.com", "john00@mail.com"],
            ["John", "johnnybravo@mail.com"],
            ["John", "johnsmith@mail.com", "john_new@mail.com"],
            ["Mary", "mary@mail.com"]]

result = accountsMerge(accounts)
print("Merged accounts:", result)
