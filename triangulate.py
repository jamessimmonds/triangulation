from determinant import withinCircle

def triangulate(graph, enclosing_triangle):
    # Algorithm

    triangles = [enclosing_triangle]

    for node in graph:
        
        #Find bad triangles
        badTriangles = []
        
        for triangle in triangles:
            p, q, r = triangle
            
            if withinCircle(node, p, q, r):
                badTriangles.append(triangle)
        
        # Find the boundaries of the polygonal hole
        polygon = []
        badEdges = []
        
        for triangle in badTriangles:
            a, b, c = triangle
            badEdges.append({a,b})
            badEdges.append({b,c})
            badEdges.append({a,c})
        
        frequencies = {}
        
        for edge in badEdges:
            edge = tuple(edge)
            if edge in frequencies.keys():
                frequencies[edge] = frequencies[edge] + 1
            else:
                frequencies[edge] = 1
                
        for key, val in frequencies.items():
            if val == 1:
                polygon.append(key)
                
        # Remove bad triangles from triangles
        for triangle in badTriangles:
            triangles.remove(triangle)
        
        # Re-triangulate the polygonal hole
        for edge in polygon:
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