class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        size = [1 for i in range(n)]
        parent = [i for i in range(n)]

        def find(n): # Return the root
            while (n != parent[n]):
                n = parent[n]
            return n

        for (u, v) in edges:
            rootU = find(u)
            rootV = find(v)

            if rootU == rootV:
                return False

            if size[u] > size[v]:
                parent[rootV] = rootU
                size[u] += size[v]
            else:
                parent[rootU] = rootV
                size[v] += size[u]

        visited = set()
        adj = {i: [] for i in range(n)}
        for (a,b) in edges:
            adj[a].append(b)
            adj[b].append(a)

        def dfs(n):
            if n in visited:
                return
            else:
                visited.add(n)
                for neighbor in adj[n]:
                    dfs(neighbor)

        dfs(0)

        return len(visited) == n