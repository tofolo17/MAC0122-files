import os

import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import numpy as np

from classes.npimage import NPImagem

os.chdir('..')


def main():
    # Declaração de Elvis
    f_name = 'images/elvis.jpg'
    image = mpimg.imread(f_name)
    gray = np.array(image)[:, :, 2]

    elvis = NPImagem((), gray)
    """
    print("elvis.shape: ", elvis.shape)
    plt.gray()
    plt.imshow(elvis.data)
    plt.show()
    """

    # Declaração de Einstein
    f_name = 'images/einstein-colorida.jpg'
    image = mpimg.imread(f_name)
    gray = np.array(image)[:, :, 2]

    einstein = NPImagem((), gray)
    """
    print("einstein.shape:", einstein.shape)
    plt.gray()
    plt.imshow(einstein.data)
    plt.show()

    # Brincadeiras

    elvis.pinte_rect(40, 30, 125, 150, v=100)
    plt.gray()
    plt.imshow(elvis.data)
    plt.show()

    elvis.paste(einstein, 40, 30)
    plt.gray()
    plt.imshow(elvis.data)
    plt.show()

    s = elvis + einstein
    plt.gray()
    plt.imshow(s.data)
    plt.show()

    s = elvis + 100
    plt.gray()
    plt.imshow(s.data)
    plt.show()
    """

    e = einstein.crop(400, 150, 500, 300)
    plt.gray()
    plt.imshow(e.data)
    plt.show()

    f = e * 100
    plt.gray()
    plt.imshow(f.data)
    plt.show()

    c = elvis.blend(einstein, 0.00001)
    plt.gray()
    plt.imshow(c.data)
    plt.show()

    exit()


main()
