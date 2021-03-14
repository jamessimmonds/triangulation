import numpy as np
import math

def theta(x, y):
    
    if (x == 0 and y >= 0):
        return math.pi * (1/2)
    elif (x == 0 and y < 0):
        return math.pi * (3/2)
    else:   
        if (x >= 0 and y >= 0): # First quadrant
            return math.atan(y/x)
        elif (x < 0 and y >= 0): # Second quadrant
            return math.atan(y/x) + math.pi
        elif (x < 0 and y < 0): # Third quadrant
            return math.atan(y/x) + math.pi
        elif (x >= 0 and y < 0): # Fourth quadrant
            return math.atan(y/x) + math.pi*2

def sort(vertices):
    
    points = []
    
    # Angles are calculated with respect to a point inside the polygon
    # A suitable point is determined by taking an average
    
    x_mean = np.mean([vertex[0] for vertex in vertices])
    y_mean = np.mean([vertex[1] for vertex in vertices])
    
    for vertex in vertices:
        points.append((vertex, theta(vertex[0]-x_mean, vertex[1]-y_mean)))
        
    sortedPoints = sorted(points, key=lambda a: a[1])
        
    return [x[0] for x in sortedPoints]