class DisjointSet:
    def __init__(self, n):
        self.rank = [0] * (n + 1)
        self.parent = list(range(n + 1))
        self.size = [1] * (n + 1)

    def find_upar(self, node):
        if node == self.parent[node]:
            return node
        self.parent[node] = self.find_upar(self.parent[node])
        return self.parent[node]

    def union_by_rank(self, u, v):
        ulp_u = self.find_upar(u)
        ulp_v = self.find_upar(v)
        if ulp_u == ulp_v:
            return
        if self.rank[ulp_u] < self.rank[ulp_v]:
            self.parent[ulp_u] = ulp_v
        elif self.rank[ulp_v] < self.rank[ulp_u]:
            self.parent[ulp_v] = ulp_u
        else:
            self.parent[ulp_v] = ulp_u
            self.rank[ulp_u] += 1

    def union_by_size(self, u, v):
        ulp_u = self.find_upar(u)
        ulp_v = self.find_upar(v)
        if ulp_u == ulp_v:
            return
        if self.size[ulp_u] < self.size[ulp_v]:
            self.parent[ulp_u] = ulp_v
            self.size[ulp_v] += self.size[ulp_u]
        else:
            self.parent[ulp_v] = ulp_u
            self.size[ulp_u] += self.size[ulp_v]


class Solution:
    def is_valid(self, adjr, adjc, n, m):
        return 0 <= adjr < n and 0 <= adjc < m

    def num_of_islands(self, n, m, operators):
        ds = DisjointSet(n * m)
        vis = [[0] * m for _ in range(n)]
        cnt = 0
        ans = []

        for it in operators:
            row, col = it[0], it[1]

            if vis[row][col] == 1:
                ans.append(cnt)
                continue

            vis[row][col] = 1
            cnt += 1

            dr = [-1, 0, 1, 0]
            dc = [0, 1, 0, -1]

            for ind in range(4):
                adjr, adjc = row + dr[ind], col + dc[ind]

                if self.is_valid(adjr, adjc, n, m) and vis[adjr][adjc] == 1:
                    node_no = row * m + col
                    adj_node_no = adjr * m + adjc

                    if ds.find_upar(node_no) != ds.find_upar(adj_node_no):
                        cnt -= 1
                        ds.union_by_size(node_no, adj_node_no)

            ans.append(cnt)

        return ans


if __name__ == "__main__":
    n, m = 4, 5
    operators = [[1,1], [0, 1], [3,3], [3,4]]

    obj = Solution()
    result = obj.num_of_islands(n, m, operators)

    for res in result:
        print(res, end=" ")
    print()
