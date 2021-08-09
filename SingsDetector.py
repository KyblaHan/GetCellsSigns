import math
import os

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

        image = cv2.imread(path)
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
        print(img.size)  # Отображаем общее количество пикселей

        rows, cols, dims = img.shape
        white_pix_count = 0
        R = 0
        G = 0
        B = 0

        for r in range(0, rows):
            for c in range(0, cols):
                if img[r, c, 0] == 255 and img[r, c, 1] == 255 and img[r, c, 2] == 255:
                    white_pix_count += 1
                else:
                    R += img[r, c, 0]
                    G += img[r, c, 1]
                    B += img[r, c, 2]

        print(white_pix_count)
        print(R/(img.size-white_pix_count))
        print(G/(img.size-white_pix_count))
        print(B/(img.size-white_pix_count))

    def get_sizes_axes_inertia(self):
        pass
