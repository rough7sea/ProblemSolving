from typing import Optional


class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def find_or_create(self, new_nodes, old_node) -> Node:
        if old_node.val not in new_nodes:
            new_nodes[old_node.val] = Node(val=old_node.val)
        return new_nodes[old_node.val]


    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        visited = [False] * 100
        queue = [node]
        new_nodes = dict()

        while queue:
            old_node: Node = queue.pop()
            visited[old_node.val] = True
            new_node = self.find_or_create(new_nodes, old_node)

            for old_neighbor in old_node.neighbors:
                if not visited[old_neighbor.val]:
                    queue.append(old_neighbor)
                new_neighbor = self.find_or_create(new_nodes, old_neighbor)
                new_node.neighbors.append(new_neighbor)
                new_neighbor.neighbors.append(new_node)

        return new_nodes[node.val]
