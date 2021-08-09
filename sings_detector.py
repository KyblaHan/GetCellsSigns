import math
import os

import numpy
import numpy as np
import cv2
from skimage import io
from skimage import segmentation
from skimage.color import rgb2gray
from skimage.filters import sobel


class SingsDetector:
    def __init__(self, path_to_img):
        self.contours, self.hierarchy = None, None
        self.path = path_to_img
        self.get_contour()

    def get_area(self):
        return cv2.contourArea(self.contours[0])

    def get_contour(self):
        path = self.path

        image = io.imread(path)
        gray = rgb2gray(image)
        elevation_map = sobel(gray)
        markers = np.zeros_like(gray)

        markers[gray < 0.7] = 1
        markers[gray > 0.83] = 2

        segment = segmentation.watershed(elevation_map, markers)


        io.imsave("temp.bmp", segment)
        # cv2.imwrite("temp.bmp", segment)

        image_g = cv2.imread("temp.bmp")

        edged = cv2.Canny(image_g, 10, 15)

        self.contours, self.hierarchy = cv2.findContours(edged, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)

        os.remove("temp.bmp")

    def get_perimeter(self):
        return cv2.arcLength(self.contours[0], True)

    def get_shape_coefficient(self):
        return 4 * math.pi * self.get_area() / (self.get_perimeter() ** 2)

    def get_average_brightness_rgb(self):
        img = io.imread(self.path)
        rows, cols, dims = img.shape
        white_pix_count = 0
        r = 0
        g = 0
        b = 0

        for row in range(0, rows):
            for col in range(0, cols):
                if (img[row, col, 0] == 255 and img[row, col, 1] == 255 and img[row, col, 2] == 255) or (img[row, col, 0] == 0 and img[row, col, 1] == 0 and img[row, col, 2] == 0):
                    white_pix_count += 1
                else:
                    g += img[row, col, 1]
                    r += img[row, col, 0]
                    b += img[row, col, 2]

        avr_r = r / (img.size - white_pix_count)
        avr_g = g / (img.size - white_pix_count)
        avr_b = b / (img.size - white_pix_count)

        return avr_r, avr_g, avr_b

    def get_std(self):
        img = io.imread(self.path)
        rows, cols, dims = img.shape
        white_pix_count = 0
        r = []
        g = []
        b = []

        for row in range(0, rows):
            for col in range(0, cols):
                if img[row, col, 0] == 255 and img[row, col, 1] == 255 and img[row, col, 2] == 255:
                    white_pix_count += 1
                else:
                    r.append(img[row, col, 1])
                    g.append(img[row, col, 0])
                    b.append(img[row, col, 2])

        std_r = numpy.std(r)
        std_g = numpy.std(g)
        std_b = numpy.std(b)

        return std_r, std_g, std_b
