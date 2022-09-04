from dijkstra import Graph, find_path
import time

G = Graph()
f = open('data2_2.txt.')
for i in range(10000):
    line = f.readline()
    line = line.strip().split(' ')
    G.add_edge(line[0], line[1], int(line[2]))
f.close()
time1 = time.time()
print(find_path(G, '0', '50'))
end_time = time.time()
time = end_time - time1
print(time)
