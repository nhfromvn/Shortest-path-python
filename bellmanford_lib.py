import networkx as nx
from bellmanford import bellman_ford
import time

G = nx.Graph()
f = open('data2_2.txt')
for i in range(10000):
    line = f.readline()
    line = line.strip().split(' ')
    G.add_edge(line[0], line[1], weight=int(line[2]))
f.close()
time1 = time.time()
print(bellman_ford(G, source='0', target='50'))
end_time = time.time()
time = end_time - time1
print(time)