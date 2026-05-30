# Definition for a Node.
class Node(object):
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution(object):
    def cloneGraph(self, node):
        if not node:
            return None
        visited = {}

        def copy(curr):
            if curr in visited:
                return visited[curr]
            new_node = Node(curr.val)
            visited[curr] = new_node
            for nb in curr.neighbors:
                new_node.neighbors.append(copy(nb))
            return new_node

        return copy(node)