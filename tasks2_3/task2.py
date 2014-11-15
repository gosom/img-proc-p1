# -*- coding: utf-8 -*-
import argparse
import sys

import numpy as np

from utils import (image2array, fft, plot, fftshift, prepare_show,
                  euclidean_distance)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('img', help=('Path of the image to perform the'
                        ' transform'))
    parser.add_argument('--rmin', type=int, help='rmin parameter', default=23)
    parser.add_argument('--rmax', type=int, help='rmax parameter', default=48)

    args = parser.parse_args()

    try:
        with open(args.img, 'rb'):
            pass
    except IOError:
        print >> sys.stderr, "%s could not be opened" % args.img
        return 1

    rmin_range = (0, 100)
    if not (rmin_range[0] < args.rmin < rmin_range[1]):
        print >> sys.stderr, "rmin should be between %d and %d" % rmin_range
        return 2

    if not (rmin_range[0] < args.rmax < rmin_range[1]):
        print >> sys.stderr, "rmax should be between %d and %d" % rmin_range
        return 2

    if args.rmin >= args.rmax:
        print >> sys.stderr, 'rmin should be less than rmax'
        return 3

    aimg = image2array(args.img)
    freq_ = fft(aimg)
    shift_freq = fftshift(freq_)

    center = (shift_freq.shape[0] / 2, shift_freq.shape[1] / 2)

    distance_array = euclidean_distance(shift_freq, center)

    mask = (distance_array < args.rmin) != (distance_array > args.rmax)

    shift_freq_cpy = shift_freq.copy()

    shift_freq_cpy[mask] = 0

    output = fft(fftshift(shift_freq_cpy, True), True)

    plot([aimg, prepare_show(shift_freq), prepare_show(shift_freq_cpy),
          prepare_show(output, False)])


if __name__ == '__main__':
    main()
