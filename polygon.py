def polygon(triangles):
    sharedEdges = []
    edges = []
    
    for triangle in triangles:
        a, b, c = triangle
        sides = [{a,b}, {b,c}, {a,c}]
        
        for side in sides:
            if side in edges:
                sharedEdges.append(side)
            else:
                edges.append(side)
                
    for edge in sharedEdges:
        edges.remove(edge)
        
    return edges