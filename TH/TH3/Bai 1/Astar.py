from collections import defaultdict

# This class represent a graph
class Graph:

    # Initialize the class
    def __init__(self, graph_dict=None, directed=True):
        self.graph_dict = graph_dict or {}
        self.directed = directed
        if not directed:
            self.make_undirected()

    # Create an undirected graph by adding symmetric edges
    def make_undirected(self):
        for a in list(self.graph_dict.keys()):
            for (b, dist) in self.graph_dict[a].items():
                self.graph_dict.setdefault(b, {})[a] = dist

    # Add a link from A and B of given distance, and also add the inverse link if the graph is undirected
    def connect(self, A, B, distance=1):
        self.graph_dict.setdefault(A, {})[B] = distance
        if not self.directed:
            self.graph_dict.setdefault(B, {})[A] = distance

    # Get neighbors or a neighbor
    def get(self, a, b=None):
        links = self.graph_dict.setdefault(a, {})
        if b is None:
            return links
        else:
            return links.get(b)

    # Return a list of nodes in the graph
    def nodes(self):
        s1 = set([k for k in self.graph_dict.keys()])
        s2 = set([k2 for v in self.graph_dict.values() for k2, v2 in v.items()])
        nodes = s1.union(s2)
        return list(nodes)


# This class represent a node
class Node:

    # Initialize the class
    def __init__(self, name: str, parent: str):
        self.name = name
        self.parent = parent
        self.g = 0  # Distance to start node
        self.h = 0  # Distance to goal node
        self.f = 0  # Total cost

    # Compare nodes
    def __eq__(self, other):
        return self.name == other.name

    # Sort nodes
    def __lt__(self, other):
        return self.f < other.f

    # Print node
    def __repr__(self):
        return ('({0},{1})'.format(self.position, self.f))

# A* search
def astar_search(graph, heuristics, start, end):
    # Create lists for open nodes and closed nodes
    open = []
    closed = []

    # Create a start node and an goal node
    start_node = Node(start, None)
    goal_node = Node(end, None)

    # Add the start node
    open.append(start_node)

    # Loop until the open list is empty
    while len(open) > 0:

        # Sort the open list to get the node with the lowest cost first
        open.sort()

        # Get the node with the lowest cost
        current_node = open.pop(0)

        # Add the current node to the closed list
        closed.append(current_node)

        # Check if we have reached the goal, return the path
        if current_node == goal_node:
            path = []
            while current_node != start_node:
                path.append(current_node.name + ': ' + str(current_node.g))
                current_node = current_node.parent
            path.append(start_node.name + ': ' + str(start_node.g))
            # Return reversed path
            return path[::-1]

        # Get neighbours
        neighbors = graph.get(current_node.name)

        # Loop neighbors
        for key, value in neighbors.items():

            # Create a neighbor node
            neighbor = Node(key, current_node)

            # Check if the neighbor is in the closed list
            if (neighbor in closed):
                continue

            # Calculate full path cost
            neighbor.g = current_node.g + graph.get(current_node.name, neighbor.name)
            neighbor.h = heuristics.get(neighbor.name)
            neighbor.f = neighbor.g + neighbor.h

            # Check if neighbor is in open list and if it has a lower f value
            for node in open:
                if (neighbor == node and neighbor.f > node.f):
                    continue

            # Everything is green, add neighbor to open list
            open.append(neighbor)

    # Return None, no path is found
    return None


# The main entry point for this module
def main():
    # Create a graph
    graph = Graph()

    file_address = input("Input file PATH: ")
    file_data = open(file_address, mode='r').read()
    file_data = file_data.split()
    file_number = int(file_data[0])
    file_data.remove(file_data[0])
    graph_size = len(file_data) - file_number
    heuristics_value = file_number

    matrix = [[0 for row in range(0, file_number)] for col in range(0, file_number)]

    # Create graph connections (Actual distance)
    for i in range(0, file_number):
        for j in range(0, file_number):
            matrix[i][j] = file_data[file_number * i + j]
            if matrix[i][j] != '0':
                graph.connect(str(i), str(j), int(matrix[i][j]))

    # Make graph undirected, create symmetric connections
    graph.make_undirected()

    # Create heuristics (straight-line distance, air-travel distance)
    heuristics = {}
    for i in range(0, heuristics_value):
        heuristics[str(i)] = int(file_data[graph_size + i])

    # Run the search algorithm
    start_vertex = str(input("Input start point: "))
    end_vertex = str(input("Input destination: "))
    path = astar_search(graph, heuristics, start_vertex, end_vertex)
    print("Path from start point to destination:", path)

# Tell python to run main method
if __name__ == "__main__": main()
