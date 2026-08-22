class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        size = [1 for i in range(n)]
        parent = [i for i in range(n)]

        if not n-1 == len(edges): 
            return False

        def find(n): # Return the root
            while (n != parent[n]):
                n = parent[n]
            return n

        for (u, v) in edges:
            rootU = find(u)
            rootV = find(v)

            if rootU == rootV:
                return False

            if size[rootU] > size[rootV]:
                parent[rootV] = rootU
                size[u] += size[v]
            else:
                parent[rootU] = rootV
                size[v] += size[u]

        return True