class Graph:
    def __init__(self):
        self.number_of_nodes = 0
        self.adjacent_list = {}
    
    def addVertex(self, value):
        self.adjacent_list[value] = []
        self.number_of_nodes += 1
    
    def addEdge(self, node1, node2):
        # Undirected graph
        if self.adjacent_list[node1] is not None and self.adjacent_list[node2] is not None:
            self.adjacent_list[node1].append(node2)
            self.adjacent_list[node2].append(node1)
        else:
            raise Exception
        
    def show_graph(self):
        for node, edges in self.adjacent_list.items():
            print(f"{node} --> {' , '.join(edges)}")

if __name__ == '__main__':
    graph = Graph()
    graph.addVertex('A')
    graph.addVertex('B')
    graph.addVertex('C')
    graph.addVertex('D')
    graph.addEdge('A', 'B')
    graph.addEdge('A', 'C')
    graph.addEdge('A', 'D')
    graph.show_graph()
    