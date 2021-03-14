from determinant import withinCircle
from polygon import polygon

def triangulate(graph, enclosing_triangle):

    triangles = [enclosing_triangle]

    for node in graph:
        
        #Find bad triangles
        badTriangles = []
        
        for triangle in triangles:
            p, q, r = triangle
            
            if withinCircle(node, p, q, r):
                badTriangles.append(triangle)
        
        # Find the boundaries of the polygonal hole
        hole = polygon(badTriangles)
                
        # Remove bad triangles from triangles
        for triangle in badTriangles:
            triangles.remove(triangle)
        
        # Re-triangulate the polygonal hole
        for edge in hole:
            a, b = edge
            newTriangle = {a, b, node}
            triangles.append(newTriangle)
            
    # Clean up
    # If a triangle contains a vertex from the super-triangle, remove it

    scaffolding = []

    for triangle in triangles:
        for vertex in triangle:
            if vertex in enclosing_triangle:
                if triangle not in scaffolding:
                    scaffolding.append(triangle)
                    
    for triangle in scaffolding:
        triangles.remove(triangle)

    return triangles