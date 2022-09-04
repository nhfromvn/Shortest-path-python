import time
from readFile import toDijstra
from readFile import toBellmanford
f=input()
g1=toDijstra(f)
time1= time.time()
g1.dijkstra(0)
print('thời gian của thuật toán Dijkstra là: '+str(time.time()-time1))
f=input()
g2= toBellmanford(f)
time2= time.time()
g2.bellman_ford(0)
print('thời gian của thuật toán Bellmanford là: '+str(time.time()-time2))
