import os
import sys
sys.path.append('src/segment')

from PyQt5 import QtWidgets, QtCore
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QFileDialog, QMessageBox
import segment as sg
import sings_worker as sw
import main_window
import sys


class mywindow(QtWidgets.QMainWindow):

    img_path = ""

    def __init__(self):

        super(mywindow, self).__init__()
        self.ui = src.main_window.Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.btn_choise_image.clicked.connect(self.btn_choise_image_clicked)
        self.ui.slider_min.valueChanged.connect(self.slider_min_valueChanged)
        self.ui.slider_max.valueChanged.connect(self.slider_max_valueChanged)
        self.ui.btn_contour.clicked.connect(self.btn_contour_clicked)
        self.ui.btn_segment.clicked.connect(self.btn_segment_clicked)
        self.ui.btn_sings.clicked.connect(self.btn_sings_clicked)

    def notification(self, text):
        """
        Генератор нотификаций
        :param text: текст нотификации
        :return:
        """

        msgBox = QMessageBox()
        msgBox.setStandardButtons(QMessageBox.Ok)
        msgBox.setText(text)
        msgBox.setWindowTitle("Внимание!")
        msgBox.exec()

    def btn_sings_clicked(self):
        sw.sings_worker("../data/segmented_cells_images").create_report()
        self.notification("Признаки расчитаны")

    def btn_segment_clicked(self):
        self.seg.test_segment()
        self.notification("Клетки сегментированны.")

    def btn_contour_clicked(self):
        self.seg = sg.segment(self.img_path)
        min_p = float(self.ui.label_min.text())
        max_p = float(self.ui.label_max.text())
        self.seg.test_contours(min_p, max_p)

        pixmap_segment = QPixmap("../data/temp/contours.bmp")
        resize_pixmap_segment = pixmap_segment.scaled(350, 350)
        self.ui.segmented_image.setPixmap(resize_pixmap_segment)

        self.notification("Контура найдены.")

    def slider_max_valueChanged(self):
        tmp = self.ui.slider_max.value()
        tmp = tmp / 100.0
        self.ui.label_max.setText(str(tmp))

    def slider_min_valueChanged(self):
        tmp = self.ui.slider_min.value()
        tmp = tmp / 100.0
        self.ui.label_min.setText(str(tmp))

    def btn_choise_image_clicked(self):
        file_path = QFileDialog.getOpenFileName(self, "Выберите файл", "data/input_images")
        self.ui.path_to_image.setText(file_path[0])

        pixmap_input_image = QPixmap(file_path[0])
        resize_pixmap_input_image = pixmap_input_image.scaled(350, 350)
        self.ui.input_image.setPixmap(resize_pixmap_input_image)

        self.img_path = file_path[0]
        segment = sg.segment(file_path[0])
        segment.create_histogram()

        pixmap_hist = QPixmap(sg.segment.path_to_histogram)
        self.ui.histogram.setPixmap(pixmap_hist)

        self.print_mins()

    def print_mins(self):
        """
        отображание основных минимумов гистограммы
        :return:
        """
        segment = sg.segment(self.img_path)
        segment.create_histogram()
        mins = segment.calc_local_min(int(self.ui.hist_sense.text()))

        self.ui.mins.setText(str(mins))

        self.ui.label_min.setText(str(mins[0]))
        self.ui.label_max.setText(str(mins[1]))


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    application = mywindow()
    application.show()

    sys.exit(app.exec())
