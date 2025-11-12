import os
import time
from graph.graph import Graph
from utils import bfs, dijkstra, cyclic

base = os.getcwd()
path = "/data/"
full_path = base + path

filenames = os.listdir(full_path)

filenames.sort()

graph_filename = []

for filename in filenames:
    graph_filename.append((Graph(full_path + filename), filename))

results = []

for graph, filename in graph_filename:
    none = str(graph.solve_none())
    some = str(graph.solve_some())
    many = str(graph.solve_many())
    few = str(graph.solve_few())
    alternate = str(graph.solve_alternate())

    
    results.append([filename, none, few, alternate, many, some])

f = open("results.txt", mode="w")

f.write(f"{'Filename':<20} {'None':<15} {'Some':<15} {'Many':<15} {'Few':<15} {'Alternate':<15} \n")
print(f"{'Filename':<20} {'None':<15} {'Some':<15} {'Many':<15} {'Few':<15} {'Alternate':<15}")
      
for result in results:
    f.write(f"{result[0]:<20} {result[1]:<15} {result[2]:<15} {result[3]:<15} {result[4]:<15} {result[5]:<15} \n")
    print(f"{result[0]:<20} {result[1]:<15} {result[2]:<15} {result[3]:<15} {result[4]:<15} {result[5]:<15}")

f.close()