
from copy import deepcopy
from utils import bfs, dijkstra, cyclic

class Graph:

    def __init__(self, path: str):
        
        file = open(path, mode="r")
        content = file.readlines()

        header = content[0].split()
        source, target = content[1].split()

        self.vertices_count = int(header[0])
        self.edges_count = int(header[1])
        self.red_count = int(header[2])

        self.vertices = []
        self.adj_list = []
        self.reds = set()
        self.vertex_to_index = {}
        self.isDirected = False

        for line in content[2:]: 
            split_line = line.split()

            if len(split_line) == 1:
                index = self.add_with_index(split_line[0])

                self.adj_list.append([])
                self.vertex_to_index[split_line[0]] = index
            
            elif len(split_line) == 2:
                index = self.add_with_index(split_line[0])
                
                self.reds.add(index)
                self.adj_list.append([])
                self.vertex_to_index[split_line[0]] = index

            elif len(split_line) == 3:
                arrow = split_line[1]
                edge_source = self.vertex_to_index[split_line[0]]
                edge_target = self.vertex_to_index[split_line[2]]

                if self.is_directed(arrow):
                    self.add_adjacent(edge_source, edge_target)
                else:
                    self.add_adjacent(edge_source, edge_target)
                    self.add_adjacent(edge_target, edge_source)

        self.source = self.vertex_to_index[source]
        self.target = self.vertex_to_index[target]
        self.isCyclic = cyclic.isCyclic(self.adj_list)

                
    def is_directed(self, line: str):
        self.isDirected = True
        return line == '->'
    
    
    def add_adjacent(self, source, target):
        # CHANGE IF YOU WANT TO DO SOMETHING USEFUL GOD DAMMIT
        self.adj_list[source].append(target)



    def add_with_index(self, element) -> int:
        index = len(self.vertices)
        self.vertices.append(element)
        return index
    
    def remove_reds(self):
        adj_list = deepcopy(self.adj_list)

        for index, vertex in enumerate(adj_list):
            if index in self.reds:
                adj_list[index] = []
                continue

            new_edges = []

            for edge in vertex:
                if edge in self.reds:
                    continue
                else:
                    new_edges.append(edge)

            adj_list[index] = new_edges

        return adj_list
    
    def weight_red(self, red_weight):
        adj_list = deepcopy(self.adj_list)

        for index, vertex in enumerate(adj_list):
            adj_list[index] = [(edge, red_weight if edge in self.reds else 0) for edge in vertex]

        return adj_list
    
    def weight_blacks(self):
        adj_list = deepcopy(self.adj_list)

        for index, vertex in enumerate(adj_list):
            adj_list[index] = [(edge, 1 if edge in self.reds else 0) for edge in vertex]

        return adj_list
    
    def make_alternated(self):
        adj_list = deepcopy(self.adj_list)

        for index, vertex in enumerate(adj_list):
            if index in self.reds:
                vertex = list(filter(lambda x: x not in self.reds, vertex))
            else:
                vertex = list(filter(lambda x: x in self.reds, vertex))
            adj_list[index] = vertex
        return adj_list
    
    def sanitize_dist(self, dist):
        return [distance if distance < 1000000 else "impossible" for distance in dist]

    def solve_none(self):
        list = self.remove_reds()
        dist = bfs.bfs(self.source, list)
        dist = self.sanitize_dist(dist)

        return dist[self.target]
    
    def solve_few(self):
        dist = dijkstra.dijk(self.weight_red(1), self.source, self.target)
        if self.source in self.reds:
            dist = dist + 1
        return dist if dist < 1000000000 else "impossible"

    def solve_alternate(self):
        list = self.make_alternated()
        dist = bfs.bfs(self.source, list)
        dist = self.sanitize_dist(dist)

        return dist[self.target]

    def solve_many(self):
        if not self.isCyclic:
            dist = abs(dijkstra.dijk(self.weight_red(-1), self.source, self.target))
            if self.source in self.reds:
                dist = dist + 1

            if dist >= 1000000000:
                dist = "impossible"
        else:
            dist = "NP hard"

        return dist

    def solve_some(self):
        if not self.isCyclic:
            dist = abs(dijkstra.dijk(self.weight_red(-1), self.source, self.target))
            
            if self.source in self.reds:
                dist = dist + 1

            if dist < 1000000000:
                dist = "True" if dist > 0 else "False"
            else:
                dist = "impossible"
        else:
            dist = "NP hard"

        return dist