import matplotlib.pyplot as plt
import numpy as np
import os

PATH_FIGURES = 'figures'

# This file should contain code ONLY related to working with figures

def make_figure(data: np.ndarray, filename: str) -> None:
    """Inputs data as a 2Xn numpy array
    """

    full_filename = os.path.join(PATH_FIGURES, filename)
    
    if not os.path.exists(PATH_FIGURES):
        os.mkdir(PATH_FIGURES)
    
    plt.figure(figsize=(6,6))
    plt.scatter(data[:, 0], data[:, 1])
    plt.savefig(full_filename, bbox_inches = ('tight'))
    plt.xlabel('x component')
    plt.ylabel('y component')
    plt.show()

    return None