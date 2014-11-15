# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import PIL.Image as PImg


def fft(data, inverse=False):
    f = np.fft.fft2 if not inverse else np.fft.ifft2
    return f(data)


def fftshift(data, inverse=False):
    f = np.fft.fftshift if not inverse else np.fft.ifftshift
    return f(data)


def image2array(fname):
    img = PImg.open(fname)
    return np.asarray(img)


def euclidean_distance(a, location):
    """credits to SO:
    http://stackoverflow.com/questions/17527340/more-efficient-way-to-calculate-distance-in-numpy
    """
    m, n = a.shape
    x_inds, y_inds = np.ogrid[:m, :n]
    return ((x_inds - location[0]) ** 2 + (y_inds - location[1]) ** 2)**0.5


def prepare_show(array, log=True):
    if log:
        return np.array(np.log10(np.abs(array)), dtype=np.uint8)
    return np.array(np.abs(array), dtype=np.uint8)


def plot(images):
    cnt = 1
    for img in images:
        plt.subplot(2, 2, cnt)
        plt.imshow(img, cmap='gray')
        plt.axis('off')
        cnt+=1
    plt.show()
