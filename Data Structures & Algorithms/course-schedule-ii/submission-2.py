class Node:
    def __init__(self, value = -1, directedTo = None):
        self.value = value
        self.directedTo = directedTo if directedTo is not None else []

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]):
        vertices = []

        for i in range(numCourses):
            vertices.append(Node(i))

        for (a,b) in prerequisites:
            vertices[a].directedTo.append(vertices[b])

        marked = [False for _ in range(numCourses)]
        onCallStack = [False for _ in range(numCourses)]
        cycleDetected = False

        def dfs(vertex):
            nonlocal cycleDetected
            marked[vertex.value] = True
            onCallStack[vertex.value] = True

            for nextVertex in vertex.directedTo:
                if cycleDetected:
                    return
                elif (not marked[nextVertex.value]):
                    dfs(nextVertex)
                elif (onCallStack[nextVertex.value]):
                    cycleDetected = True

            onCallStack[vertex.value] = False

        for vertex in vertices:
            if not marked[vertex.value]:
                dfs(vertex)

        return (not cycleDetected, vertices)


    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        finishable, vertices = self.canFinish(numCourses, prerequisites)

        if not finishable: return []

        marked = [False for _ in range(numCourses)]
        reversePost = [] # Stack

        def dfs(node):
            marked[node.value] = True
            for nei in node.directedTo:
                if not marked[nei.value]:
                    dfs(nei)
            reversePost.append(node.value)

        for vertex in vertices:
            if not marked[vertex.value]:
                dfs(vertex)

        return reversePost
