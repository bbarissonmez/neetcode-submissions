class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj_list = {i:[] for i in range(n)}
        marked = [False for _ in range (n)]

        for (a,b) in edges:
            adj_list[b].append(a)
            adj_list[a].append(b)

        count = 0

        def dfs(node):
            marked[node] = True
            for neighb in adj_list[node]:
                if not marked[neighb]:
                    dfs(neighb)

            
        for node in range(n):
            if not marked[node]:
                dfs(node)
                count +=1

        return count