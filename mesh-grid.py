import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

if __name__ == "__main__":
    X = np.linspace(-5, 5, 11)
    Y = np.linspace(-5, 5, 11)
    xx, yy = np.meshgrid(X, Y)
    print(xx)
    print(yy)
    Z = 4 * xx ** 2 + yy ** 2
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(xx, yy, Z, cmap="plasma", linewidth=0, antialiased=False, alpha=0.5)
    plt.show()
