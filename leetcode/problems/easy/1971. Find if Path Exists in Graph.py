from typing import List


class Node:
    def __init__(self, value):
        self.value = value
        self.visited = False
        self.edges = []


class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if source == destination:
            return True
        graph_map = {}

        for edge in edges:
            self.put_or_create(graph_map, edge[0], edge[1])
            self.put_or_create(graph_map, edge[1], edge[0])

        if source not in graph_map or destination not in graph_map:
            return False

        queue = []
        node = graph_map[source]
        while node is not None:
            for edge in node.edges:
                if edge == destination:
                    return True

                next_node: Node = graph_map[edge]
                if next_node.visited:
                    continue

                next_node.visited = True
                queue.append(next_node.value)

            if len(queue) > 0:
                node = graph_map[queue.pop(0)]
            else:
                node = None

        return False

    def put_or_create(self, graph_map, from_node, to_node):
        if from_node in graph_map:
            node: Node = graph_map[from_node]
            if to_node not in node.edges:
                node.edges.append(to_node)
        else:
            graph_map[from_node] = Node(from_node)
            graph_map[from_node].edges.append(to_node)


sol = Solution()
print(sol.validPath(n=6, edges=[[0, 1], [0, 2], [3, 5], [5, 4], [4, 3]], source=0, destination=5))
