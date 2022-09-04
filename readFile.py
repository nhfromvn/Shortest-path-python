from Dijkstra import Graph
from Bellmanford import Graph2
def toDijstra(inputFile):
    f = open(str(inputFile))
    num_of_vertices = int(f.readline())
    g= Graph(num_of_vertices)
    for i in range(num_of_vertices):
        line = f.readline()
        splitline = line.strip().split(' ')
        g.add_edge(int(splitline[0]), int(splitline[1]), int(splitline[2]))
    f.close()
    return g
def toBellmanford(inputFile):
    f = open(str(inputFile))
    num_of_vertices = int(f.readline())
    g= Graph2(num_of_vertices)
    for i in range(num_of_vertices):
        line = f.readline()
        splitline = line.strip().split(' ')
        g.add_edge(int(splitline[0]), int(splitline[1]), int(splitline[2]))
    f.close()
    return g