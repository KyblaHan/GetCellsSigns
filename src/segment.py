import pathlib

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
        """
        Генерация гистограммы
        :return:
        """
        image = io.imread(self.path)
        gray = rgb2gray(image)

        self.hist, self.hist_centers = histogram(gray)

        fig, axes = plt.subplots()
        axes.plot(self.hist_centers, self.hist, lw=2)
        plt.xticks(np.arange(0, 1, 0.1))
        axes.minorticks_on()
        #  Определяем внешний вид линий основной сетки:
        axes.grid(which='major', color="k")
        #  Определяем внешний вид линий вспомогательной сетки:
        axes.grid(which='minor', linestyle=':')

        plt.savefig(self.path_to_histogram)

    def calc_local_min(self, sense):
        """
        Поиск локального минимума
        :param sense: Чувствительность
        :return: List  минимумов
        """
        mins = []
        extrm = argrelextrema(self.hist, np.less, order=sense)
        for item in extrm[0]:
            mins.append(self.hist_centers[item])
        return mins

    def calc_local_min_dynamic_sence(self):
        """
        Поиск первых 2х минимумов. Чувствительность растет от 1 до 200
        :return:
        """
        mins = []

        for sense in range(1, 200):
            extrm = argrelextrema(self.hist, np.less, order=sense)
            if len(extrm[0]) == 2:
                break

        extrm = argrelextrema(self.hist, np.less, order=sense)
        for item in extrm[0]:
            mins.append(self.hist_centers[item])
        return mins

    def test_contours(self, min_p, max_p):
        """
        Поиск контуров
        :param min_p: нижний порог
        :param max_p: верхний порог
        :return:
        """
        image = io.imread(self.path)
        gray = rgb2gray(image)

        elevation_map = sobel(gray)

        markers = np.zeros_like(gray)
        markers[gray < min_p] = 1
        markers[gray > max_p] = 2

        segmentation_1 = segmentation.watershed(elevation_map, markers)

        fig, ax = plt.subplots(figsize=(4, 3))
        ax.imshow(segmentation_1, cmap=plt.cm.gray)

        io.imsave("data/temp/segment.bmp", segmentation_1)

        image = cv2.imread(self.path)
        image_g = cv2.imread("data/temp/segment.bmp")
        edged = cv2.Canny(image_g, 10, 15)

        cv2.imwrite("data/temp/canny edges.bmp", edged)

        contours, hierarchy = cv2.findContours(edged, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
        self.contours = contours
        cv2.drawContours(image, contours, -1, (0, 255, 0), 3)
        cv2.imwrite("data/temp/contours.bmp", image)


    def test_segment(self):
        """
        Сегментация
        :return:
        """

        img = cv2.imread(self.path)
        # img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        print(len(self.contours))
        for i in range(0, len(self.contours)):
            if cv2.contourArea(self.contours[i]) > 3000:
                idx = i  # The index of the contour that surrounds your object
                mask = np.zeros_like(gray)  # Create mask where white is what we want, black otherwise
                cv2.drawContours(mask, self.contours, idx, 255, -1)  # Draw filled contour in mask
                out = np.zeros_like(img)  # Extract out the object and place into output image
                out[mask == 255] = img[mask == 255]
                # Now crop
                (y, x) = np.where(mask == 255)
                (topy, topx) = (np.min(y), np.min(x))
                (bottomy, bottomx) = (np.max(y), np.max(x))
                out = out[topy:bottomy + 1, topx:bottomx + 1]

                cv2.imwrite('data\segmented_cells_images\Output' + str(i) + ".bmp", out)


