def find_provinces(n, roads):
    def dfs(city, visited):
        visited[city] = True
        for neighbor in range(n):
            if roads[city][neighbor] == 1 and not visited[neighbor]:
                dfs(neighbor, visited)

    visited = [False] * n
    province_count = 0

    for city in range(n):
        if not visited[city]:
            province_count += 1
            dfs(city, visited)

    return province_count

# Example Usage
if __name__ == "__main__":
    # Sample input
    n = 4
    roads = [ [1, 1, 1, 0],
            [1, 1, 1, 0],
            [1, 1, 1, 0],
            [0, 0, 0, 1] ]

    # Find the number of provinces
    provinces = find_provinces(n, roads)

    print("Number of provinces:", provinces)
