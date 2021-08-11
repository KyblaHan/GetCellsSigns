import math
import os

import numpy
import numpy as np
import cv2
from skimage import io
from skimage import segmentation
from skimage.color import rgb2gray
from skimage.filters import sobel


class sings_detector:
    """
    Класс поиска признаков на сегментированном изображении.
    """
    path = "data/temp/temp_input.bmp"
    columns = ["area", "perimeter", "shape_coefficient", "average_brightness_rgb", "std"]

    def __init__(self, path_to_img):
        self.contours, self.hierarchy = None, None
        self.base_path = path_to_img
        self.black_to_white()
        self.get_contour()

    def black_to_white(self):
        """
        Замена черных пикселей на белые.
        :return:
        """
        img = cv2.imread(self.base_path)
        black = np.where((img[:, :, 0] <= 0) & (img[:, :, 1] <= 0) & (img[:, :, 2] <= 0))
        img[black] = (255, 255, 255)
        cv2.imwrite(self.path, img)

    def get_all_signs(self):
        """
        Функция поиска всех признаков.
        :return: list всех признаков
        """
        output_data = [self.get_area(), self.get_perimeter(), self.get_shape_coefficient(),
                       self.get_average_brightness_rgb(), self.get_std()]

        return output_data

    def get_area(self):
        """
        площадь
        :return:
        """
        return cv2.contourArea(self.contours[0])

    def get_contour(self):
        """
        поиск контура
        :return:
        """
        path = self.path

        image = io.imread(path)
        gray = rgb2gray(image)
        elevation_map = sobel(gray)
        markers = np.zeros_like(gray)

        markers[gray < 0.7] = 1
        markers[gray > 0.83] = 2

        segment = segmentation.watershed(elevation_map, markers)

        io.imsave("data/temp/temp.bmp", segment)
        # cv2.imwrite("temp.bmp", segment)

        image_g = cv2.imread("data/temp/temp.bmp")

        edged = cv2.Canny(image_g, 10, 15)

        self.contours, self.hierarchy = cv2.findContours(edged, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)

        os.remove("data/temp/temp.bmp")

    def get_perimeter(self):
        """
        периметр
        :return:
        """
        return cv2.arcLength(self.contours[0], True)

    def get_shape_coefficient(self):
        """
        коэффициент формы (4*Пи*S/(Р**2))
        :return:
        """
        return 4 * math.pi * self.get_area() / (self.get_perimeter() ** 2)

    def get_average_brightness_rgb(self):
        """
        средняя яркость по цветовым компонентам RGB
        :return:
        """
        img = io.imread(self.path)
        rows, cols, dims = img.shape
        white_pix_count = 0
        r = 0
        g = 0
        b = 0

        for row in range(0, rows):
            for col in range(0, cols):
                if (img[row, col, 0] == 255 and img[row, col, 1] == 255 and img[row, col, 2] == 255) or (
                        img[row, col, 0] == 0 and img[row, col, 1] == 0 and img[row, col, 2] == 0):
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
        """
        СКО по цветовым компонентам RGB
        :return:
        """
        img = io.imread(self.path)
        rows, cols, dims = img.shape
        white_pix_count = 0
        r = []
        g = []
        b = []

        for row in range(0, rows):
            for col in range(0, cols):
                if img[row, col, 0] == 255 and img[row, col, 1] == 255 and img[row, col, 2] == 255 or (
                        img[row, col, 0] == 0 and img[row, col, 1] == 0 and img[row, col, 2] == 0):
                    white_pix_count += 1
                else:
                    r.append(img[row, col, 1])
                    g.append(img[row, col, 0])
                    b.append(img[row, col, 2])

        std_r = numpy.std(r)
        std_g = numpy.std(g)
        std_b = numpy.std(b)

        return std_r, std_g, std_b
