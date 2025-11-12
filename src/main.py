import os
import time
from graph.graph import Graph
from utils import bfs, dijkstra

def sanitize_dist(dist):
    return [distance if distance < 10000 else "impossible" for distance in dist]

base = os.getcwd()
path = "/data/"
full_path = base + path

filenames = os.listdir(full_path)

filenames.sort()

graph_filename = []

for filename in filenames:
    graph_filename.append((Graph(full_path + filename), filename))

for graph, filename in graph_filename:
    tag = "NO REDS"
    search_start = time.time()
    list = graph.remove_reds()
    dist = bfs.bfs(graph.source, list)
    search_end = time.time()

    dist = sanitize_dist(dist)

    search_time = (search_end - search_start) * 1000
    print(f"{tag:<15} {filename:<20} Distance: {dist[graph.target]:<20} Searching: {search_time:>8.2f} ms")

for graph, filename in graph_filename:
    tag = "FEWEST REDS ON PATH"
    search_start = time.time()
    dist = dijkstra.dijk(graph.weight_red(), graph.source, graph.target)
    search_end = time.time()

    if graph.source in graph.reds:
        dist = dist + 1

    dist = dist if dist < 1000000000 else "impossible"

    search_time = (search_end - search_start) * 1000
    print(f"{tag:<20} {filename:<20} Amount of reds: {dist:<20} Searching: {search_time:>8.2f} ms")
