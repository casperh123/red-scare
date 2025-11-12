import os
import time
from graph.graph import Graph
from utils import bfs

base = os.getcwd()
path = "/data/"
full_path = base + path

filenames = os.listdir(full_path)

for filename in filenames:
    file_start = time.time()
    graph = Graph(full_path + filename)
    file_end = time.time()

    search_start = time.time()
    dist = bfs.bfs(graph.source, graph.adj_list)
    search_end = time.time()

    parsing_time = (file_end - file_start) * 1000
    search_time = (search_end - search_start) * 1000
    print(f"{filename:<20} Distance: {dist[graph.target]:<10} Parsing: {parsing_time:>8.2f} ms  Searching: {search_time:>8.2f} ms")