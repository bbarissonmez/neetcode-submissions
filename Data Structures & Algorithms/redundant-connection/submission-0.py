class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        size = [1 for i in range(1, len(edges)+1)]
        parent = [i for i in range(1, len(edges)+1)]

        def find(n): # Return the root
            while (n != parent[n-1]):
                n = parent[n-1]
            return n

        for (u, v) in edges:
            rootU = find(u)
            rootV = find(v)

            if rootU == rootV:
                return [u, v]

            if size[rootU-1] > size[rootV-1]:
                parent[rootV-1] = rootU
                size[u-1] += size[v-1]
            else:
                parent[rootU-1] = rootV
                size[v-1] += size[u-1]

        