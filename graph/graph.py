class Graph:
  def __init__(self, edges, isDirected):
    self.adjacencyList = edges
    self.isDirected = isDirected
    self.length = len(edges)

  def edges(self, vertex):
    return self.adjacencyList(vertex)
  


