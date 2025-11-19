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
    none =      graph.solve_none()
    some =      graph.solve_some()
    many =      graph.solve_many()
    few =       graph.solve_few()
    alternate = graph.solve_alternate()

    
    results.append([filename, none, some, many, few, alternate])

f = open("results.txt", mode="w")

f.write(f"{'Filename':<20} {'None':>15} {'Some':>15} {'Many':>15} {'Few':>15} {'Alternate':>15}")
f.write(f"{'None Time':>15} {'Some Time':>15} {'Many Time':>15} {'Few Time':>15} {'Alternate Time':>15} \n")
print(f"{'Filename':<20} {'None':<15} {'Some':<15} {'Many':<15} {'Few':<15} {'Alternate':<15}")
      
for result in results:
    f.write(f"{result[0]:<20} {result[1][0]:>15} {result[2][0]:>15} {result[3][0]:>15} {result[4][0]:>15} {result[5][0]:>15}")
    f.write(f"{str(round(result[1][1],4))+"s":>15} {str(round(result[2][1],4))+"s":>15} {str(round(result[3][1],4))+"s":>15} {str(round(result[4][1],4))+"s":>15} {str(round(result[5][1],4))+"s":>15} \n")
    print(f"{result[0]:<20} {result[1][0]:>15} {result[2][0]:>15} {result[3][0]:>15} {result[4][0]:>15} {result[5][0]:>15}")

f.close()