import os
import time
from graph.graph import Graph
from utils import bfs, dijkstra, cyclic


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

# Problem: None
for graph, filename in graph_filename:
    tag = "NONE"
    search_start = time.time()
    list = graph.remove_reds()
    dist = bfs.bfs(graph.source, list)
    search_end = time.time()

    dist = sanitize_dist(dist)

    search_time = (search_end - search_start) * 1000
    print(f"{tag:<15} {filename:<20} Distance: {dist[graph.target]:<20} Searching: {search_time:>8.2f} ms")

# Problem: Few
for graph, filename in graph_filename:
    tag = "FEW"
    search_start = time.time()
    dist = dijkstra.dijk(graph.weight_red(1), graph.source, graph.target)
    search_end = time.time()

    if graph.source in graph.reds:
        dist = dist + 1

    dist = dist if dist < 1000000000 else "impossible"

    search_time = (search_end - search_start) * 1000
    print(f"{tag:<15} {filename:<20} Amount of reds: {dist:<20} Searching: {search_time:>8.2f} ms")

# Problem: Alternate
for graph, filename in graph_filename:
    tag = "ALTERNATE"
    search_start = time.time()
    list = graph.make_alternated()
    dist = bfs.bfs(graph.source, list)
    search_end = time.time()
    
    dist = sanitize_dist(dist)

    search_time = (search_end - search_start) * 1000
    print(f"{tag:<15} {filename:<20} Distance: {dist[graph.target]:<20} Searching: {search_time:>8.2f} ms")
    

# Problem: Many
for graph, filename in graph_filename:
    tag = "MANY"
    search_start = time.time()
    if not graph.isCyclic:
        dist = abs(dijkstra.dijk(graph.weight_red(-1), graph.source, graph.target))
        if graph.source in graph.reds:
            dist = dist + 1

        if dist >= 1000000000:
            dist = "impossible"
    else:
        dist = "NP hard"

    search_end = time.time()

    search_time = (search_end - search_start) * 1000
    print(f"{tag:<15} {filename:<20} Amount of reds: {dist:<20} Searching: {search_time:>8.2f} ms")

    # IDEA: if we modified dijkstra to store the currently taken path on a given bfs and checked whether the vertex currently being searched is part of the noted path, the solution may work for cyclic graphs.


    # Problem: Some
for graph, filename in graph_filename:
    tag = "SOME"
    search_start = time.time()
    if not graph.isCyclic:
        dist = abs(dijkstra.dijk(graph.weight_red(-1), graph.source, graph.target))
        
        if graph.source in graph.reds:
            dist = dist + 1

        if dist < 1000000000:
            dist = "True" if dist > 0 else "False"
        else:
            dist = "impossible"
    else:
        dist = "NP hard"
    search_end = time.time()

    search_time = (search_end - search_start) * 1000
    print(f"{tag:<15} {filename:<20} Path exists: {(dist):<20} Searching: {search_time:>8.2f} ms")
