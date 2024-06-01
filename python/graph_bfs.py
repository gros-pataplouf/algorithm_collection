class Node:
    def __init__(self, data, edges) -> None:
        self.data = data
        self.edges = []

def visit(node):
    print(node.data)

def bfs(root):
    visited_nodes = set()
    nodes_to_visit = []
    nodes_to_visit.append(root)
    visited_nodes.add(root)
    visit(root)
    while nodes_to_visit:
        current_node = nodes_to_visit.pop()
        for child in current_node.edges:
            visit(child)
            if not child in visited_nodes:
                visited_nodes.add(child)
                nodes_to_visit.insert(0,child)
