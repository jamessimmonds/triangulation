import matplotlib.pyplot as plt

def drawTriangles(triangles):
    for triangle in triangles:
        a,b,c = triangle
    
        x_vals_1 = [a[0], b[0]]
        y_vals_1 = [a[1], b[1]]
        x_vals_2 = [b[0], c[0]]
        y_vals_2 = [b[1], c[1]]
        x_vals_3 = [c[0], a[0]]
        y_vals_3 = [c[1], a[1]]

        plt.plot(x_vals_1, y_vals_1)
        plt.plot(x_vals_2, y_vals_2)
        plt.plot(x_vals_3, y_vals_3)
    
    plt.show()