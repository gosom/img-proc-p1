# -*- coding: utf-8 -*-
import argparse
import sys

import numpy as np

from utils import (image2array, fft, plot, get_magnitude, get_phase,
                   image_from_mag_phase, prepare_show)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('img1', help=('Image1'))
    parser.add_argument('img2', help=('Image2'))

    args = parser.parse_args()

    images = (args.img1, args.img2)
    for img in images:
        try:
            with open(img, 'rb'):
                pass
        except IOError:
            print >> sys.stderr, "%s could not be opened" % img
            return 1

    img1, img2 = image2array(images[0]), image2array(images[1])

    if img1.shape != img2.shape:
        print >> sys.stderr, "Images should have the same dimensions"
        return 2

    G, H = fft(img1), fft(img2)

    magG = get_magnitude(G)
    phaseH = get_phase(H)

    K = image_from_mag_phase(magG, phaseH)

    img3 = fft(K, True)
    plot([img1, img2, prepare_show(img3, False)])

    return 0


if __name__ == '__main__':
    sys.exit(main())
