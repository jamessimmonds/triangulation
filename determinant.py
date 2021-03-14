import numpy as np

from anticlockwise import sort

# Is s within the circle cimcumscribing abc?
def withinCircle(s, a, b, c):
    
    # For this definition to be valid, abc must be sorted anticlockwise
    vertices = [a,b,c]
    p, q, r = sort(vertices)
    
    sx = s[0]
    sy = s[1]
    px = p[0]
    py = p[1]
    qx = q[0]
    qy = q[1]
    rx = r[0]
    ry = r[1]
    
    arr = np.array([
        [px, py, px**2+py**2, 1],
        [qx, qy, qx**2+qy**2, 1],
        [rx, ry, rx**2+ry**2, 1],
        [sx, sy, sx**2+sy**2, 1]
    ])
    
    return np.linalg.det(arr) >= 0