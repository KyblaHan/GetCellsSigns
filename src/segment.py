import cv2
import matplotlib.pyplot as plt
import numpy as np
from scipy import ndimage
from scipy.signal import argrelextrema
from skimage import io
from skimage import segmentation
from skimage.color import rgb2gray
from skimage.exposure import histogram
from skimage.feature import canny
from skimage.filters import sobel


class segment:
    path_to_histogram = 'data/temp/histogram.png'

    def __init__(self, path):
        self.path = path

    def create_histogram(self):
        image = io.imread(self.path)
        gray = rgb2gray(image)

        hist, hist_centers = histogram(gray)

        fig, axes = plt.subplots()
        axes.plot(hist_centers, hist, lw=2)
        plt.xticks(np.arange(0, 1, 0.1))
        axes.minorticks_on()
        #  Определяем внешний вид линий основной сетки:
        axes.grid(which='major', color="k")
        #  Определяем внешний вид линий вспомогательной сетки:
        axes.grid(which='minor', linestyle=':')

        plt.savefig(self.path_to_histogram)
