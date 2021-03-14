import random

from triangulate import triangulate
from draw import drawTriangles

max_x = 2000
max_y = 2000
nodes = 50

graph = []

for node in range(0, nodes):
    x = random.randrange(0, max_x)
    y = random.randrange(0, max_y)
    
    graph.append((x,y))

enclosing_triangle = {(-2000,-100), (4000,-100), (1000, 4000)}

triangles = triangulate(graph, enclosing_triangle)
drawTriangles(triangles)